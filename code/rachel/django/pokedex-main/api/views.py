import pokemon
from rest_framework import generics, viewsets
from pokemon.models import Pokemon, Type
from .serializers import PokemonSerializer

class PokemonAPIView(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer




