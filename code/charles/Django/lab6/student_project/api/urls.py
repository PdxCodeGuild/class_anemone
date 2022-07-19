from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('students', views.StudentApiView, basename='students')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('api/v1/students/<int:student_id>', views.StudentApiView.as_view(), name='students')
]