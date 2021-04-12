from django.db import models


# Create your models here.

# TODO: Create an Employee model with properties required by the user stories

class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    route_zipcode = models.CharField(max_length=9, default=53154)

    def __str__(self):
        return self.name
