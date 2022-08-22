from django.urls import path
from .views import ListPokemon, DetailPokemon, CurrentUserView
from . import views







urlpatterns = [
    path('', ListPokemon.as_view()),


    path('<int:pk>/', DetailPokemon.as_view()),


    path('current-user/', CurrentUserView.as_view()),
]

