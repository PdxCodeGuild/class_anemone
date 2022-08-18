from django.urls import path 
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostView.as_view(), name='posts'),
    path('posts/', views.PostCreateView.as_view(), name='create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]