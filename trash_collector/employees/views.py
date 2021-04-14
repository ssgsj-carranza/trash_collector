from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from .models import Employee
import datetime
# from ..customers.models import Customer
from os import path
from django.shortcuts import get_object_or_404


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
    user = request.user
    Customer = apps.get_model('customers.Customer')
    all_customers = Customer.objects.all()
    in_zip = []
    context = {'customer': in_zip}
    for customer in all_customers:
        if customer.pick_up_zip == Employee.route_zipcode:
            in_zip.append(customer)
    return render(request, 'employees/customer_in_zip.html', context)


# customers_in_zip = customers.filter(address__zip_code__contains = employee.zip_code)

def today_pick_up(request):
    Customer = apps.get_model('customers.Customer')
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    today_customer = Customer.objects.get(date__range=(today_min, today_max))
    # return today_customer
    return render(request, 'employees/today_pick_up.html', today_customer)


def extra_today_pick_up(request):
    Customer = apps.get_model('customers.Customer')
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    extra_customer = Customer.objects.get(date__range=(today_min, today_max))
    # return extra_customer
    return render(request, 'employees/today_pick_up.html', extra_customer)


def non_suspended_account(request):
    Customer = apps.get_model('customers.Customer')
    all_customers = Customer.objects.all()
    non_suspended = []
    context = {'customers': non_suspended}
    for customer in all_customers:
        if Customer.customer_account_active is True:
            non_suspended.append(customer)
    return render(request, 'employees/non_suspended_accounts.html', context)


# might need to work on function below, not quite sure it's correct
def confirm_charge(request):
    user = request.user
    Customer = apps.get_model('customers.Customer')
    specific_customer = Customer.objects.get(user_id=user.id)
    context = {'customer': specific_customer}
    if request.method == 'POST':
        specific_customer.current_bill += request.POST.get('amount_charged')
        specific_customer.save()
    return render(request, 'employees/confirm_charge.html', context)
