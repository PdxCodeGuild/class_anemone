from django.urls import path

from . import views

app_name = 'chirp'

urlpatterns = [
    path('', views.ChirpListView.as_view(), name='home'),
    path('chirp/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    path('chirp/new/', views.ChirpCreateView.as_view(), name='new'),
    path('chirp/<int:pk>/edit/', views.ChirpEditView.as_view(), name='edit'),
    path('chirp/<int:pk>/delete/', views.ChirpDeleteView.as_view(), name='delete'),
]