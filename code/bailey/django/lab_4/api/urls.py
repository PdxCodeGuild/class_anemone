from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateStudentAPIView.as_view()),
    path('<int:pk>/', views.RUDStudentAPIView.as_view()),
]