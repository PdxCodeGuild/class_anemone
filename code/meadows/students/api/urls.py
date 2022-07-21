from django.urls import path

from .views import StudentAPIView, StudentViewSet

urlpatterns = [
    path('', StudentAPIView.as_view()),
    path('<int:pk>/', StudentViewSet.as_view()),
]
