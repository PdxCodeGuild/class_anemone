from django.urls import path

from . import views

app_name = 'grocery_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add'),
    path('update/<int:pk>/', views.update_item, name='update'),
    path('delete/<int:pk>/', views.delete_item, name='delete'),
]
