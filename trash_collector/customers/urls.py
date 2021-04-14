from django.urls import path, include

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('table_of_customers/', views.table_of_customers, name='table_of_customers'),
    path('suspend/<int:customer_id>', views.suspend, name='suspend'),
    path('info/', views.info, name='info'),
    path('change_pickup_date/', views.change_pickup_date, name='change_pickup_date'),
    path('one_time_pick_up/', views.spec_pickup, name='one_time_pick_up')
]
