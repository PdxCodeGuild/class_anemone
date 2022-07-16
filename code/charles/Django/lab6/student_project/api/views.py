from django.shortcuts import render
from rest_framework import viewsets, permissions
from students.models import Student
from .serializers import StudentSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsUsernameOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsUsernameOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Create your views here.
