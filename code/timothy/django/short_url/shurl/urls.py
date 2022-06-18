from django.urls import path
from . import views

app_name = 'shurl'

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/<int:short_url_id>/', views.shorten, name='shorten'),
]