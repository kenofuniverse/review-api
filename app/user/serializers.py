from rest_framework import serializers
from app.user.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'email']
