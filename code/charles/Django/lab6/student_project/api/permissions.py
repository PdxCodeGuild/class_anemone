from math import perm
from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsSuper(permissions.BasePermission):
    def has_permission(self, request, view):
        print('superuser')
        return request.user.username == 'cgt10'

class IsUsernameOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.first_name == request.user