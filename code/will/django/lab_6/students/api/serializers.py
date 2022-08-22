from rest_framework import serializers

from students_app.models import Student

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','firstname', 'lastname', 'cohort', 'favorite_topic', 'favorite_teacher' )