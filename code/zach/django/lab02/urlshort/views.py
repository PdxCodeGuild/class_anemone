from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page_view(request):
    name ="zach"
    return render(request, "base.html")