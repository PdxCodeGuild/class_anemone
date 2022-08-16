from rest_framework import generics, viewsets, permissions
from pokemon.models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsSuper, IsRegisteredOrReadOnly
from django.shortcuts import render

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [IsRegisteredOrReadOnly]

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsRegisteredOrReadOnly]

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsRegisteredOrReadOnly]

class CurrentUserViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
