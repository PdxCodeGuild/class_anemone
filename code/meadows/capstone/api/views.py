from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model
from mygympal.models import Blog
from .serializers import UserSerializer
from .permissions import IsSuper, IsRegisteredOrReadOnly


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsRegisteredOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
