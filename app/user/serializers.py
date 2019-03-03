from rest_framework import serializers
from app.user.models import User

class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['id', 'username', 'full_name']
