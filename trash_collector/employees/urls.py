from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('customer_in_zip/', views.customer_in_zip, name='customer_in_zip'),
    path('today_pick_up/', views.today_pick_up, name='today_pick_up'),
    path('extra_today_pick_up/', views.extra_today_pick_up, name='extra_today_pick_up'),
    # path('non_suspended_accounts/', views.non_suspended_account, name='non_suspended_accounts')
]