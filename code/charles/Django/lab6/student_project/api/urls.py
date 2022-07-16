from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('student', views.StudentViewSet, basename='student')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls