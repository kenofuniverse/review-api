from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
  # User username
  username = models.CharField(
    max_length=256,
    null=False,
    unique=True
  )
  # User firstname
  first_name = models.CharField(
    max_length=256,
    null=False
  )
  # User lastname
  last_name = models.CharField(
    max_length=256,
    null=False
  )

  USERNAME_FIELD = 'username'
