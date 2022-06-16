from cmath import atanh
from django.urls import URLPattern, path
from . import views

app_name = 'short_url'

urlpatterns =  [
    path('', views.index, name='index'),
    path('shorten/', views.shorten, name='shorten')
]