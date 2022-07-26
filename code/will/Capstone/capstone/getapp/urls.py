from django.urls import path
from . import views



urlpatterns = [
    path('', views.zillow, name = 'zillow'),
]