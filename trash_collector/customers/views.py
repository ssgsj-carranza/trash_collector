from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from django.urls import reverse
from django.shortcuts import get_object_or_404


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.

def index(request):
    # get the logged in user within any view function
    user = request.user
    all_customers = Customer.objects.all()
    context = {
        'all_customers': all_customers
    }
    # This will be useful while creating a customer to assign the logged in user as the user foreign key
    # Will also be useful in any function that needs
    print(user)
    return render(request, 'customers/index.html', context)


def table_of_customers(request):
    all_customers = Customer.objects.all()
    context = {
        'all_customers': all_customers
    }
    return render(request, 'customers/table.html', context)


def suspend(request):
    user = request.user
    specific_customer = Customer.objects.get(user_id=user.id)
    if request.method == 'POST':
        specific_customer.is_active = False
        specific_customer.save()
        return HttpResponseRedirect(reverse('customer:index'))
    return render(request, 'customers/suspend.html')


def change_pickup_date(request):
    user = request.user
    specific_customer = Customer.objects.get(user_id=user.id)
    if request.method == 'POST':
        specific_customer.pickup_date = request.POST.get('pickup_date')
        specific_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers.pickup_date.html')


def spec_pickup(request):
    user = request.user
    specific_customer = Customer.objects.get(user_id=user.id)
    if request.method == 'POST':
        specific_customer.one_time_pick_up = request.POST.get('one_time_pick_up')
        specific_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/one_time_pick_up.html')


# https://docs.djangoproject.com/en/1.8/intro/tutorial02/


def info(request):
    user = request.user
    specific_customer = get_object_or_404(Customer, user_id=user.id)
    if request.method == 'POST':
        specific_customer.current_bill += request.POST.get('amount_charged')

    # show pickup?
    # context = {}
    # if request.method == 'POST':
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/info.html')


def create(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        pick_up_zip = request.POST.get('pick_up_zip')
        pickup_date = request.POST.get('pickup_date')
        new_customer = Customer(name=name, pickup_date=pickup_date, pick_up_zip=pick_up_zip, address=address)
        new_customer.user_id = user.id
        new_customer.save()
        return HttpResponseRedirect(reverse('customer:index'))
    else:
        return render(request, 'customers/create.html')


