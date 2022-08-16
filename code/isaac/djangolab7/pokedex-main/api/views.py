from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model
from pokemon.models import Pokemon, Type 
from .serializers import PokemonSerializer, TypeSerializer, CustomUserSerializer
from .permissions import IsAuthorOrReadyOnly

class PokemonView(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [IsAuthorOrReadyOnly]

class TypeView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthorOrReadyOnly]

class PokemonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentUser(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user

