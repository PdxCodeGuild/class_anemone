from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'students.html'
    