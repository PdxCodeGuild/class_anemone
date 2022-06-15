from django.urls import path
from . import views

app_name = 'grocery_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:item_id>/markcomplete/', views.markcomplete, name='markcomplete'),
    path('<int:item_id>/delete/', views.delete, name='delete')
]