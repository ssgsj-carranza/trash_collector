from django.db import models


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    pick_up_date = models.DateTimeField('date of pick up')

    def __str__(self):
        return self.name


class ChoiceDays(models.Model):
    date = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pick_up_choice = models.CharField(max_length=20)
