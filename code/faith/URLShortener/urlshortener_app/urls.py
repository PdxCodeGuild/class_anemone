from django.urls import path
from . import views

app_name = 'urlshortener_app' 
urlpatterns = [
    path('', views.index, name='index'),
    path('urlshortener_app/<str:short_url>/', views.redirect, name='redirect')
]