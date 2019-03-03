from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
  """
    Model for User
  """
  full_name = models.CharField(
    max_length=256,
    null=False
  )

  email = models.EmailField(
    unique=True
  )

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['full_name']
