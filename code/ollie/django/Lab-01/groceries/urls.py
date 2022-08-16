from django.urls import path

from django.utils import timezone

from . import views

app_name = 'groceries'
urlpatterns = [
    path('', views.index, name='index'),
    # path('create/', views.create, name='create'),
]
