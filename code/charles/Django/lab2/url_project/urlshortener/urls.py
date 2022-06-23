from django.urls import path
from . import views

app_name = 'urlshortener'

urlpatterns = [
    path('<str:kurl>', views.direct, name='direct'), 
    path('', views.index, name='index'),
    path('newurl/', views.newurl, name='newurl'),
    
]