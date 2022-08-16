from django.urls import path

from django.utils import timezone

from . import views

app_name = 'groceries'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete')
]
