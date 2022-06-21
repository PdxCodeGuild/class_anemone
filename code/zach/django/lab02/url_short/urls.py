from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/', views.url_short, name='index')
]
