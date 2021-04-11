from django.urls import path, include

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('suspend/<int:customer_id>', views.suspend, name='suspend'),
    path('info/<int:customer_id>', views.info, name='info'),
    path('update/<int:customer_id', views.update, name='update')
]
