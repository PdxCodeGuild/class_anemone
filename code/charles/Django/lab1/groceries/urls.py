from django.urls import path

from . import views

app_name = 'groceries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:glist_id>/', views.detail, name='detail'), 
    path('<int:glist_id>/list/', views.detail, name='list'), 
     
]