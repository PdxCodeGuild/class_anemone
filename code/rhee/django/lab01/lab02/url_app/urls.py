from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name = 'home'),
    path('<str:new_url>', views.short, name = 'short')

]
