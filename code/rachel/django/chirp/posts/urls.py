from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.ChirpListView.as_view(), name='home'),
    path('post/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    path('post/create/', views.ChirpCreateView.as_view(), name='create'),
    path('post/<int:pk>/delete/', views.ChirpDeleteView.as_view(), name='delete')
]