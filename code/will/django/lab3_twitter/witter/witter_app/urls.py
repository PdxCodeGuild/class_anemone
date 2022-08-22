from django.urls import path
from . import views

app_name = 'witter_app'

urlpatterns = [
    path('', views.WitterListView.as_view(), name='home'),
    path('witter_app/<int:pk>/', views.WitterDetailView.as_view(), name='detail'),
    path('witter_app/new/', views.WitterCreateView.as_view(), name='create'),
    path('witter_app/<int:pk>/edit', views.WitterUpdateView.as_view(), name='update'),
    path('witter_app/<int:pk>/delete/', views.WitterDeleteView.as_view(), name='delete'),



]