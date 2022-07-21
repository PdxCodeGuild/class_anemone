from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')

urlpatterns = router.urls
# + [
#     path('', views.StudentViewSet.as_view())
# ]