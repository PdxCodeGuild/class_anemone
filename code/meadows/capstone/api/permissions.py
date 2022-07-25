
from rest_framework import permissions
from users.models import CustomUser

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsSuper(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return request.user.username == 'jj'

class IsRegisteredOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated