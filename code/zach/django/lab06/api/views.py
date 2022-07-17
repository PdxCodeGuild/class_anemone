from rest_framework.response import Response
from rest_framework.decorators import api_view
from students.models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def getData(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)