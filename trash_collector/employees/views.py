from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from .models import Employee
import datetime
# from ..customers.models import Customer
from os import path


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')


def create(request):
    if request.method == 'POST':
        print(request)
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
    customer: object = apps.get_model('customers.Customer')
    customers = customer.objects.all()
    in_zip = []
    for customer in customers:
        if customer.route_zipcode == request.POST.get('route_zipcode'):
            in_zip.append(customer)
    return HttpResponseRedirect(reverse('employees:index'))


# customers_in_zip = customers.filter(address__zip_code__contains = employee.zip_code)

def today_pick_up():
    Customer = apps.get_model('customers.Customer')
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    today_customer = Customer.objects.get(date__range=(today_min, today_max))
    return today_customer


def extra_today_pick_up():
    Customer = apps.get_model('customers.Customer')
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    extra_customer = Customer.objects.get(date__range=(today_min, today_max))
    return extra_customer

# https://realpython.com/transaction-management-with-django-1-6/
# def non_suspended_account():
#     Customer = apps.get_model('customers.Customer')
#     customers = Customer.objects.all()
#     non_suspended = []
#     for customer in customers:
#         if Customer.suspend_start_date and Customer.suspend_end_date
