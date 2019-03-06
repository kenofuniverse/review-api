from rest_framework import generics, permissions

from . import models
from . import serializers
from .permissions import IsReviewer

class ReviewListView(generics.ListCreateAPIView):

  serializer_class = serializers.ReviewSerializer
  permission_classes = (permissions.IsAuthenticated, IsReviewer)

  def get_queryset(self):
    return models.Review.objects.filter(reviewer=self.request.user)
