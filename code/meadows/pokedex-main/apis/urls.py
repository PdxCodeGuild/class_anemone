from django.urls import path

from .views import PokemonAPIView, PokemonViewSet, TypeViewSet

urlpatterns = [
    path('', PokemonAPIView.as_view()),
    path('<int:pk>/', PokemonViewSet.as_view()),
    path('type', TypeViewSet.as_view())
]