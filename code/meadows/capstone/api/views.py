from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.contrib.auth import get_user_model
from mygympal.models import Blog
from .serializers import UserSerializer, BlogSerializer
from .permissions import IsSuper, IsRegisteredOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # parser_classes = (MultiPartParser, FormParser)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsRegisteredOrReadOnly]
    # parser_classes = (MultiPartParser, FormParser)



class CurrentUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsRegisteredOrReadOnly]

# class CurrentBlogView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BlogSerializer
#     def get_object(self):
#         return self.request