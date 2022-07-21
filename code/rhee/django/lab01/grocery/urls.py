
from django.urls import path
from . import views

app_name = 'grocery'

urlpatterns = [
    path('',views.home, name='home'),
    path('create/', views.create,name='create'),
    path('complete/<int:pk>/', views.complete, name='complete'),
    path('delete/<int:pk>/', views.delete, name='delete')
]