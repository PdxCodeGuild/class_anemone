from django.shortcuts import render
from requests import post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post

# for listing out the chirps on the homepage
class ChirpListView(ListView):
    model = Post 
    template_name = 'home.html'
