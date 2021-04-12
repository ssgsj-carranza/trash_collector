from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from .models import Employee


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.method.POST.get('name')
        zip_code = request.POST.get('zip code')
        new_employee = Employee(name=name, zip_code=zip_code)
        new_employee.user_id = user.id
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


def customer_in_zip(request):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    customer: object = apps.get_model('customer.Customer')
    customers = customer.objects.all()
    in_zip = []
    for customer in customers:
        if customer.pick_up_zip ==
