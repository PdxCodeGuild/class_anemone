from rest_framework import generics

from pokemon.models import Pokemon, Type
from .serializers import PokemonSerlializer, ClassSerlializer

class PokemonAPIView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerlializer

class PokemonViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerlializer

class TypeViewSet(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = ClassSerlializer

