from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls