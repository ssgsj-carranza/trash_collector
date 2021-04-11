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
    # This will be useful while creating a customer to assign the logged in user as the user foreign key
    # Will also be useful in any function that needs
    print(user)
    return render(request, 'customers/index.html')


def table_of_customers(request):
    all_customers = Customer.objects.all()
    context = {
        'all_customers': all_customers
    }
    return render(request, 'customers/table.html', context)


def suspend(request, customer_id):
    context = {}
    specific_customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        specific_customer.delete()
        return HttpResponseRedirect(reverse('customer:table'))
    context['customer'] = specific_customer
    return render(request, 'customers/suspend.html', context)


def 