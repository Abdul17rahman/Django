from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="index"),
    path('greet/<str:name>', views.greet, name="greet"),
    path('greet/', views.greet, name="greets")
]