from rest_framework import generics

from . import models
from . import serializers

class CompanyListView(generics.ListCreateAPIView):

  queryset = models.Company.objects.all()
  serializer_class = serializers.CompanySerializer
