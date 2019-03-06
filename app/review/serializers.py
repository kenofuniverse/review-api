from rest_framework import serializers
from app.review.models import Review
from app.company.models import Company
from app.company.serializers import CompanySerializer
from app.user.serializers import CustomUserSerializer

class ReviewSerializer(serializers.ModelSerializer):
  company = CompanySerializer(read_only=True)
  reviewer = CustomUserSerializer(read_only=True)

  class Meta:
    model = Review
    fields = ['id', 'rating', 'title', 'summary', 'ip_address', 'submission_date', 'company', 'reviewer']
    read_only_fields = ['ip_address']
  
  def create(self, validated_data):
    request = self.context.get('request')
    user = request.user
    ip_address = request.META.get('REMOTE_ADDR')

    review = Review(**validated_data)
    review.ip_address = ip_address
    review.reviewer = user
    review.save()

    return review
