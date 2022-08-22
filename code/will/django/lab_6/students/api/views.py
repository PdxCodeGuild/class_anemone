

from rest_framework import generics

from students_app.models import Student

from .serializers import PostSerializer


class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = PostSerializer
 

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = PostSerializer
    


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = PostSerializer