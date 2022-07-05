from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('newpost', views.newpost, name='newpost'),
    path('edited', views.edited, name='edited'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('bsignup', views.bsignup, name = 'bsignup')
]