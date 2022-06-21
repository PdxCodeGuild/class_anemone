from django.urls import path

from . import views

app_name = 'short_url'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('redirect/<int:code>/', views.redirect, name='redirect'),
    # path('<int:code>/redirect/', views.redirect, name='redirect'),
]