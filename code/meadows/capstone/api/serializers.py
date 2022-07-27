from rest_framework import serializers
from django.contrib.auth import get_user_model
from mygympal.models import Blog
from users.models import CustomUser

class NestedBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'created', 'updated')

class UserSerializer(serializers.ModelSerializer):
    user_detail = NestedBlogSerializer(many=True, source='posts', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',  'profile_pic', 'user_detail')