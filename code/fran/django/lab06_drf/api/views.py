from rest_framework import generics

from students.models import Student
from .serializers import StudentSerializer

class ListCreateStudentAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RUDStudentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
