from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):

  # User firstname
  full_name = models.CharField(
    max_length=256,
    null=False
  )
