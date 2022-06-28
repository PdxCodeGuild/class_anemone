from django.urls import path
from . import views

app_name = 'url_shortener'

urlpatterns = [
    path('url_shortener', views.index, name='index'),
    path('redirect/<str:short_url>', views.redirect, name='redirect'),
]