from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Chirp, User

# Create your views here.
class PostView(ListView):
    model = Chirp
    template_name = "posts.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    fields = ['head', 'body']
    template_name = "new_post.html"

    def form_valid(self, form):
        print(form)
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Chirp
    template_name = "detail.html"

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = 'delete.html'
    success_url = reverse_lazy('posts:posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user
