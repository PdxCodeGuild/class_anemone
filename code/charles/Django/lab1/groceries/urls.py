from django.urls import path, include

from . import views

app_name = 'groceries'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createitem, name='createitem'),
    path('delete/', views.delete, name='delete'),
    path('deleteitem/', views.deleteitem, name='deleteitem'),
    path('status/', views.status, name='status'),
    path('statusupdate/', views.statusupdate, name='statusupdate'),
]