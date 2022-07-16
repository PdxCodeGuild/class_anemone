from django.contrib.auth import get_user_model
from students.models import Student
from rest_framework import serializers

class NestedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'cohort')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class StudentSerializer(serializers.ModelSerializer):
    student_detail = NestedStudentSerializer(read_only=True, source='username')
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'student_detail', 'cohort', 'favorite_topic', 'favorite_teacher', 'capstone')

class UserSerializer(serializers.ModelSerializer):
    student_detail = NestedUserSerializer(many=True, source='student', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'student', 'student_detail')