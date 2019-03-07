from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse
from model_mommy import mommy
from mock import MagicMock

from app.review.models import Review
from app.review.permissions import IsReviewer
from app.company.models import Company
from app.user.models import CustomUser

class ReviewTests(APITestCase):
  def setUp(self):
    self.user = CustomUser.objects.create_user(
      'tester',
      'tester@example.com',
      'Test123'
    )
    self.company = mommy.make(
      Company,
      name='Fake Company',
      description='A Fake Company'
    )
    self.url = reverse('review-list-view')
    self.permission = IsReviewer
    self.request = MagicMock(user=MagicMock())
    self.view = MagicMock()

  def login(self):
    token = Token.objects.get(user=self.user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
  
  def dummy_review(self):
    return {
      'title': 'Dummy Review',
      'summary': 'This is Dummy Review',
      'rating': 1,
      'company_id': self.company.id
    }

  def dummy_bad_review(self):
    return {
      'title': 'Dummy Review',
      'summary': 'This is Dummy Review',
      'rating': 7, # must be between 1-5
      'company_id': self.company.id
    }

  def test_permission_is_reviewer(self):
    # Should be false for non reviewers
    org = MagicMock()
    self.assertFalse(self.permission.has_object_permission(self, self.request, self.view, org))

  def test_get_reviews_from_empty_reviews(self):
    # Should get empty array
    self.login()
    response = self.client.get(self.url, format='json')

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, [])

  def test_create_review(self):
    # Should increase review count and last review be same as the mock data
    before_count = Review.objects.all().count()

    self.login()
    response = self.client.post(
      self.url,
      self.dummy_review()
    )

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Review.objects.all().count(), before_count + 1)

    last_review = Review.objects.last()

    self.assertEqual(last_review.title, 'Dummy Review')
    self.assertEqual(last_review.summary, 'This is Dummy Review')
    self.assertEqual(last_review.rating, 1)
    self.assertEqual(last_review.reviewer, self.user)
    self.assertEqual(last_review.company, self.company)

  def test_create_bad_review(self):
    # Should return bad request for bad review
    self.login()
    response = self.client.post(
      self.url,
      self.dummy_bad_review()
    )

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_get_reviews(self):
    # Should get reviews posted
    self.login()

    response = self.client.post(self.url, self.dummy_review())
    review_id = response.data.get('id')
    reviewer = response.data.get('reviewer')

    response = self.client.get(self.url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data[0]['id'], review_id)
    for review in response.data:
      self.assertEqual(review['reviewer']['id'], reviewer['id'])
  
  def test_get_reviews_from_non_authenticated_user(self):
    # Should get 403 Forbidden
    response = self.client.get(self.url, format='json')
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_get_reviews_from_other_user(self):
    # Should not get reviews posted by other users
    dummyUser1 = mommy.make(CustomUser, username='dummyUser1')
    dummyUser2 = mommy.make(CustomUser, username='dummyUser2')
    mommy.make(Review, reviewer=dummyUser1)
    mommy.make(Review, reviewer=dummyUser2)
    mommy.make(Review, reviewer=dummyUser1)
    mommy.make(Review, reviewer=dummyUser2)
    my_reviews = [
      mommy.make(Review, reviewer=self.user),
      mommy.make(Review, reviewer=self.user),
      mommy.make(Review, reviewer=self.user)
    ]

    self.login()

    response = self.client.get(self.url)
    self.assertEqual(len(response.data), len(my_reviews))
    for review, returned_review in zip(my_reviews, reversed(response.data)):
      self.assertEqual(review.id, returned_review['id'])

  def test_review_str(self):
    review = mommy.make(Review, title='Fake Review') 
    self.assertEqual(str(review), 'Fake Review')
