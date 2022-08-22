from django import views
from django.urls import path
from . import views

app_name = 'short_url'

urlpatterns = [
    path('', views.index, name='index'),
    path('code', views.code, name='code'),
    path('redirect', views.redirect, name='redirect')
]