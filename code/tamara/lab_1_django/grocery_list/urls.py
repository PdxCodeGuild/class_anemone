from django import views
from django.urls import path 
from . import views

app_name = 'grocery_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.create, name='create'),
    path('', views.complete, name='complete'),
    path('', views.delete, name='delete')
]