
from django.urls import path 

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.ListView.as_view(),name='home'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('post/create', views.CreateView.as_view(), name='create'),
    path('post/<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.DeleteView.as_view(), name='delete')
]