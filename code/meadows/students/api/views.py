from rest_framework import generics

from students.models import Student
from .serializers import StudentsSerializer

class StudentAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class StudentViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

# Create your views here.
