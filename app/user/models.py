from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  """
    Model for User
  """
  description = models.TextField(blank=True)
