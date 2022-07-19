from django.urls import path
from . import views

urlpatterns = [
    path('', views.PokemonAPIView.as_view()),
    
]
