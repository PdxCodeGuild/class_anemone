from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.TwitListView.as_view(), name='home'),
    path('posts/<int:pk>/', views.TwitDetailView.as_view(), name='detail'),
    path('posts/new/', views.TwitCreateView.as_view(), name='new'),
    path('posts/<int:pk>/edit/', views.TwitEditView.as_view(), name='edit'),
    path('posts/<int:pk>/delete/', views.TwitDeleteView.as_view(), name='delete'),
]