from rest_framework import generics, viewsets, permissions
from pokemon.models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer
from django.contrib.auth import get_user_model

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CurrentUserViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user