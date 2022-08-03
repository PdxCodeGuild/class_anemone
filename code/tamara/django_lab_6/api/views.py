from rest_framework import generics, viewsets

from students.models import Student
from .serializers import StudentSerializer

# class StudentAPIView(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentViewSet (viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class CurrentUserView(generics.RetrieveAPIView):
#     serializer_class = StudentSerializer
#     def get_object(self):
#         return self.request.user
