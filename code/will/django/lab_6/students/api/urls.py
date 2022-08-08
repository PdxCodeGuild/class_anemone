from django.urls import path

from . import views



urlpatterns = [
    path('', views.StudentAPIView.as_view()),
    path('students/<int:pk>', views.StudentDetails.as_view()),
    path('students/', views.StudentList.as_view()),

]