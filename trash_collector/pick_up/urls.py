from . import views
from django.urls import path, include

app_name = "pick_up"
urlpatterns = [
    path('', views.index, name="index")
]