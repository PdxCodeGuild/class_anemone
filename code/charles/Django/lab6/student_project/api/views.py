from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from students.models import Student
from .serializers import StudentSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsUsernameOrReadOnly
from .serializers import serializers

class StudentViewSet(viewsets.ModelViewSet):
    # search_fields = ['first_name', 'last_name', 'cohort', 'favorite_teacher', 'favorite_topic', 'capstone']
    # filter_backends = (filters.SearchFilter)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsUsernameOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user


# Create your views here.
