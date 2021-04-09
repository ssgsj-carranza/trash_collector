from django.db import models


# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=100, default=0)
    city = models.CharField(max_length=100, default=0)
    state = models.CharField(max_length=20, default=0)
    zip_code = models.CharField(max_length=9, default=0)
