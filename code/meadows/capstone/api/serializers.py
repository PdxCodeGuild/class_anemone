from rest_framework import serializers
from django.contrib.auth import get_user_model
from mygympal.models import Blog
from users.models import CustomUser



class NestedBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'created', 'updated', 'body')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_pic')

class BlogSerializer(serializers.ModelSerializer):
    user_detail = NestedUserSerializer(read_only=True, source='username')
    class Meta:
        model = Blog
        fields = ('title', 'username', 'user_detail', 'created', 'updated', 'body')


class UserSerializer(serializers.ModelSerializer):
    blog_detail = NestedBlogSerializer(many=True, source='posts', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',  'profile_pic', 'blog_detail')