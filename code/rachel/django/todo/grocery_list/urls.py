from django.urls import path
from . import views

app_name = 'to_do'

urlpatterns = [
    path('', views.index, name='index')
]