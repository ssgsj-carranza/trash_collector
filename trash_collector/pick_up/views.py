from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from django.shortcuts import render


# Create your views here.

def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')
