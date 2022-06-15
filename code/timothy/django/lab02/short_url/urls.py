from django.urls import path
from . import views

app_name = 'short_url'

urlpatterns = [
    path('', views.index, name='index')
]