from rest_framework import generics

from . import models
from . import serializers

class CompanyListView(generics.ListCreateAPIView):
  """
  get:
    Return a list of all companies available

  post:
    Create a new company
  """
  queryset = models.Company.objects.all()
  serializer_class = serializers.CompanySerializer
