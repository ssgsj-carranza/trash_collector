from django.db import models


# Create your models here.
class PickUp(models.Model):
    name_of_pick_up = models.CharField(max_length=50)
    date_of_pick_up = models.CharField(max_length=50)
    address_of_pick_up = models.CharField(max_length=50)

    def __str__(self):
        return self.name_of_pick_up
