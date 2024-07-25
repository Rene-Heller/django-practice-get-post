from locale import currency
from django.db import models

# Create your models here.
class Gadget(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0.0)
    currency = models.CharField(max_length=3, default="USD")