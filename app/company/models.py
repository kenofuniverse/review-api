from django.db import models

class Company(models.Model):
  """
    Model for Company
  """
  name = models.CharField(
    max_length = 256,
    unique=True,
    null = False
  )

  description = models.TextField(blank=True)

  verbose_name_plural = 'companies'

  def __str__(self):
    return self.name
