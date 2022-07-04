from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('new_account', views.new_account, name='new_account'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('editprofile', views.editprofile, name='editprofile')
]