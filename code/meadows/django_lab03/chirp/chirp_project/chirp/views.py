import re
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'chirp/index.html', context)

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
    else:
        return render(request, 'chirp/signup.html')