import pokemon
from rest_framework import generics
from pokemon.models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer

class PokemonAPIView(generics.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer




