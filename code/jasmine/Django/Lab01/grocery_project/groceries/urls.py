from django.urls import path
from . import views


app_name='groceries'

urlpatterns = [
    path('', views.index, name='index')
]