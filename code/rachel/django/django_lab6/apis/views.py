from rest_framework import generics, viewsets
from students.models import Student
from .serializers import StudentSerializer

class ListStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
