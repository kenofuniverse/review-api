from rest_framework import serializers
from app.review.models import Review

class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = ['id', 'rating', 'title', 'summary', 'ip_address', 'submission_date']
