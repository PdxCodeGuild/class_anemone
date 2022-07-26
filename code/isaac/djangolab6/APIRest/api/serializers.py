from rest_framework import serializers
from django.contrib.auth import get_user_model

from student.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'cohort', 'favorite_topic', 'favorite_teacher', 'capstone')
