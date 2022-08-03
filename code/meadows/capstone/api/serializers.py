from rest_framework import serializers
from django.contrib.auth import get_user_model
from mygympal.models import Blog
from users.models import CustomUser
from mygympal.models import Blog

# class NestedBlogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ('title', 'body', 'created', 'updated')

# class UserSerializer(serializers.ModelSerializer):
#     user_detail = NestedBlogSerializer(many=True, source='posts', read_only=True)
#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'username',  'profile_pic', 'user_detail')


# -------------------------------------------------


class NestedBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'created', 'updated', 'body')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'profil_pic')

class PostSerializer(serializers.ModelSerializer):
    user_detail = NestedUserSerializer(many=True, read_only=True, source='username')
    class Meta:
        model = Blog
        fields = ('title', 'user_detail', 'created', 'updated', 'body')

        # def create(self, validate_data):
        #     user_data = validate_data.pop('user_detail')
        #     blog = Blog.objects.create(**validate_data)

        #     for user in user_data:
        #         get_user_model().objects.create(blog=blog, **user)

class UserSerializer(serializers.ModelSerializer):
    blog_detail = NestedBlogSerializer(many=True, source='posts', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',  'profile_pic', 'blog_detail')