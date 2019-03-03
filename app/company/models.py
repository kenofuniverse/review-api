from django.db import models

class Company(models.Model):
  """
    Model for Company
  """
  name = models.CharField(
    max_length = 256,
    null = False
  )

  company_id = models.CharField(
    max_length = 256,
    null = False
  )
