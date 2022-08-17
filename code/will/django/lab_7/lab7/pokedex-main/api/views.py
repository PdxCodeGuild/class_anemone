from django.shortcuts import render
from rest_framework import generics 
from pokemon import models
from .serializers import CustomUserSerializer, PokemonSerializer



class ListPokemon(generics.ListCreateAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer


class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class CurrentUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user



