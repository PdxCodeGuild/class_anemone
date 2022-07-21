from django.shortcuts import render

from students.models import Student
# Create your views here.
from rest_framework import viewsets, generics

from students import models
from .serializers import StudentSerializer

# class StudentAPIView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer