from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='register'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile')
]