from django.shortcuts import render, get_object_or_404, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions, generics, serializers, filters, status
from students.models import Student
from .serializers import StudentSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsSuper, IsUsernameOrReadOnly



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsUsernameOrReadOnly]
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['first_name', 'last_name', 'cohort', 'favorite_teacher', 'favorite_topic', 'capstone']
    # ordering_fields = ['=name', 'last_name']
    # ordering_fields = ['first_name', 'last_name', 'cohort', 'favorite_teacher', 'favorite_topic', 'capstone']
    # ordering = ['id']  

    # def get_object(self, student_id):
    #     try:
    #         return Student.objects.get(id=student_id)
    #     except Student.DoesNotExist:
    #         return None

    # def get(self, request, student_id, *arg, **kwargs):
    #     studentinst = self.get_object(student_id)
    #     if not studentinst:
    #         return Response({"res": "Student id does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    #     serializer = StudentSerializer(studentinst)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def put(self, request, student_id, *args, **kwargs):
    #     studentinst = self.get_object(student_id)
    #     if not studentinst:
    #         return Response({"res": "Student id does not exist"}, status=status.HTTP_404_NOT_FOUND)
    #     data = {
    #         'first_name': request.data.get('first_name'), 
    #         'last_name': request.data.get('last_name'), 
    #         'cohort': request.data.get('cohort'), 
    #         'favorite_teacher': request.data.get('favorite_teacher'), 
    #         'favorite_topic': request.data.get('favorite_topic'), 
    #         'capstone': request.data.get('capstone')
    #     }
    #     serializer= StudentSerializer(instance=studentinst, data=data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    # def delete(self, request, student_id, *args, **kwargs):
    #     studentinst = self.get_object(student_id)
    #     if not studentinst:
    #         return Response({"res": "Student id does not exist"}, status=status.HTTP_404_NOT_FOUND)
    #     studentinst.delete()
    #     return Response({"res": "Student Removed"}, status=status.HTTP_200_OK)

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsSuper]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user







# Create your views here.
