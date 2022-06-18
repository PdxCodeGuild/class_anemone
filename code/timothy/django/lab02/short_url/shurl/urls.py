from django.urls import path 
from . import views

app_name = 'shurl'

urlpatterns = [
    path('', views.index, name='index'),
    path('shortened/', views.shortened, name='shortened'),
]