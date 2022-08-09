import pokemon
from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model
from pokemon.models import Pokemon, Type
from .serializers import CustomUserSerializer, PokemonSerializer, TypeSerializer
from .permissions import IsAuthorOrReadyOnly


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [IsAuthorOrReadyOnly]

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_class = [IsAuthorOrReadyOnly]

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    def get_object(self):
        return self.request.user




