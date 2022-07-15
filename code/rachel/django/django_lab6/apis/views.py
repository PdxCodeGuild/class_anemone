from rest_framework import generics
from students.models import Student
from .serializers import StudentSerializer

class ListStudent(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer