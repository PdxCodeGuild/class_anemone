from rest_framework import generics, viewsets, permissions

from pokemon.models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer



