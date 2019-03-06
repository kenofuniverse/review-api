from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

from app.user.models import CustomUser
from app.company.models import Company

class Review(models.Model):
  class Meta:
    ordering = ('-submission_date', )

  rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  title = models.CharField(max_length=64)
  summary = models.CharField(max_length=10000)
  ip_address = models.GenericIPAddressField()
  submission_date = models.DateTimeField(auto_now_add=True)

  company = models.ForeignKey(
    Company,
    on_delete=models.PROTECT
  )
  reviewer = models.ForeignKey(
    CustomUser,
    null=True,
    on_delete=models.SET_NULL
  )

  def __str__(self):
    return self.title
