import re
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'chirp/index.html', context)

# def create(request):
