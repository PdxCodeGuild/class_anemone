from django.urls import path
from . import views

app_name = 'grocerylist_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('complete/<int:pk>/', views.complete, name='complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]