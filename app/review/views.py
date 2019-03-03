from rest_framework import generics

from . import models
from . import serializers

class ReviewListView(generics.ListCreateAPIView):

  queryset = models.Review.objects.all()
  serializer_class = serializers.ReviewSerializer
