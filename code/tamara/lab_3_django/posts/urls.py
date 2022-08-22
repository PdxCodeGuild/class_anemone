from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [ 
    path('', views.ChirpListView.as_view(), name='home'),
    path('post/new/', views.ChirpCreateView.as_view(), name='new'),
    path('post/<int:pk>/delete/', views.ChirpDeleteView.as_view(), name='delete'),
]