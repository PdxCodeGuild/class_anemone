from django.urls import path
from . import views


app_name = 'getapp' 



urlpatterns = [
    path('', views.new, name = 'new' ),
    path('intermediate/', views.zillow, name = 'intermediate')
]