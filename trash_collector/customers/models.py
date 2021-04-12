from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=1, on_delete=models.CASCADE)
    pickup_date = models.CharField(max_length=50, default=0)
    one_time_pick_up = models.DateField(null=True, blank=True)
    suspend_start_date = models.DateField(null=True, blank=True)
    suspend_end_date = models.DateField(null=True, blank=True)
    current_bill = models.FloatField(default=0)
    pick_up_charge_amount = models.FloatField(default=0)
    pick_up_zip = models.CharField(max_length=9, default=53154)
    address = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name


# class ChoiceDays(models.Model):
#     date = models.ForeignKey(Customer, default=1, on_delete=models.CASCADE)
#     pick_up_choice = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.pick_up_choice
