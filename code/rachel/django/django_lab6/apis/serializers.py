from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'cohort',
            'fav_topic',
            'fav_teacher',
            'capstone',
        )
        model = Student