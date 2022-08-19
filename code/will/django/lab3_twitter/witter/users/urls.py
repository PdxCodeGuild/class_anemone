from importlib.resources import path
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('str:username>/', views.UserProfileView.as_view(), name='profile'),
    path('logout/', views.SignupView.as_view, name='logout'),




]