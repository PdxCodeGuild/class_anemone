from django.urls import path

from . import views

app_name='users'

urlpatterns = [
    path('create_account/', views.CreateAccountPage.as_view(), name='create_account'),
    path('<str:username>/', views.ProfilePage.as_view(), name='profile'),
]