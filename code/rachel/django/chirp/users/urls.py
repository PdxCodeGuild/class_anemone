from django.urls import path

from . import views

app_name='users'

urlpatterns = [
    path('signup/', views.SignUpPage.as_view(), name='signup'),
    path('<str:username>/', views.ProfilePage.as_view(), name='profile'),
]