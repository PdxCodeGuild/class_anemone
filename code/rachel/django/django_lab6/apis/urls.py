from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListStudent.as_view()),
]
