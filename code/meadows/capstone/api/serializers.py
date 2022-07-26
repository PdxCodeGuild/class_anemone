from rest_framework import serializers
from django.contrib.auth import get_user_model
from mygympal.models import Blog
from users.models import CustomUser

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title','created', 'updated', 'body')

class UserSerializer(serializers.ModelSerializer):
    user_detail = NestedUserSerializer(many=True, source='posts', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')   