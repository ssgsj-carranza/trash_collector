from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# for test purposes
def index(request):
    return HttpResponse("Hi")
