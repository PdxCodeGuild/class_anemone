from django.urls import path
from . import views

app_name ='lab1'

urlpatterns = [
    path('', views.index, name ='index'),
    path('create/', views.create, name='create'),
    path('complete/<int:pk>/', views.complete, name ='complete'),
    path('delete/<int:pk>/', views.delete, name='delete')
]