from django.db import models

from app.user.models import User

class Review(models.Model):
  rating = models.IntegerField()
  title = models.CharField(max_length=64)
  summary = models.TextField()
  ip_address = models.CharField(max_length=15)
  submission_date = DateField()
