from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("status/", views.Status, name="Status"),
]