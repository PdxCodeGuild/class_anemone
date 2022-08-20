from django.urls import path
from .views import ListPokemon, DetailPokemon, CurrentUserView
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pokemons', views.PokemonViewSet, basename='pokemons')


urlpatterns = router.urls + [
    path('base/', ListPokemon.as_view()),


    path('base/<int:pk>/', DetailPokemon.as_view()),


    path('current-user/', CurrentUserView.as_view()),
]

