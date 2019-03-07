from rest_framework import generics, permissions

from . import models
from . import serializers
from .permissions import IsReviewer

class ReviewListView(generics.ListCreateAPIView):
  """
  get:
    Return a list of all reviews submitted by the current user

  post:
    Create a new review under current user
  """
  serializer_class = serializers.ReviewSerializer
  permission_classes = (permissions.IsAuthenticated, IsReviewer)

  def get_queryset(self):
    return models.Review.objects.filter(reviewer=self.request.user)
