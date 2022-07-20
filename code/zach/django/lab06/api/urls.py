from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.StudentViewSet, basename='students')
urlpatterns = router.urls


# urlpatterns = [
#     path('add', views.addStudent),
#     path('all', views.ListStudent.as_view()),
#     path('<int:pk>/', views.DetailStudent.as_view()),
# ]