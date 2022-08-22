from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import witter_app

class WitterListView(ListView):
    model = witter_app
    template_name = 'home.html'


class WitterDetailView(DetailView):
    model = witter_app
    template_name = 'witter_detail.html'

class WitterCreateView(CreateView):
    model = witter_app
    template_name = 'witter_new_post.html'
    fields = ['title', 'body']

class WitterUpdateView(UpdateView):
    model = witter_app
    template_name = 'witter_update.html'
    fields = ['title', 'body']

class WitterDeleteView(DeleteView):
    model = witter_app
    template_name = 'witter_delete.html'
    success_url = reverse_lazy('posts:home')