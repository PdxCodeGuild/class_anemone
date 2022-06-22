from django.urls import path

from . import views

app_name = "short_url"

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:createurl>/', views.createurl, name='createurl'),
    path('<str:newurl>/', views.newurl, name='newurl')
]