from django.urls import path
from . import views

app_nname = 'url_shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:code>', views.redirect, name='redirect'),
]