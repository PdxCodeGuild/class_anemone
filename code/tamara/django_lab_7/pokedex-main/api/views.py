from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer
from .permissions import IsAuthenticatedOrReadOnly, ReadOnly

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [ReadOnly]

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user