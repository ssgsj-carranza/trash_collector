from . import views
from django.urls import path

app_name = 'address'
urlpatterns = [
    path('index', views.index, name='index')
]

# might need to change index later?