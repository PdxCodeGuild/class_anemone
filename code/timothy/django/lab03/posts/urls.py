from django.urls import path 
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.ListChirps.as_view(), name='home'),
    path('posts/create/', views.CreateChirp.as_view(), name='create')
]