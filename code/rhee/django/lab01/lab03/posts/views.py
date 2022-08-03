from django.shortcuts import render
from dataclasses import field
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Posts

class ListView(ListView):
    model = Posts
    template_name = 'home.html'

class DetailView(DetailView):
    model = Posts
    template_name = 'detail.html'

class CreateView(CreateView):
    model = Posts
    template_name = 'create.html'
    fields = ['author','body']

class EditView(UpdateView):
    model = Posts
    template_name = 'edit.html'
    fields = ['title', 'body']

class DeleteView(DeleteView):
    model = Posts
    template_name = 'delete.html'
    success_url = reverse_lazy('posts:home')