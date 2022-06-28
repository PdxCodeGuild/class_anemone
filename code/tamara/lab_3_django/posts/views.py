from django.shortcuts import render
from requests import post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# for listing out the chirps on the homepage
class ChirpListView(ListView):
    model = Post 
    template_name = 'home.html'

# class for seeing all the chirps of a user on their user page
class UserView(ListView):
    model = Post
    template_name = 'user_detail.html'

class ChirpCreateView (LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_chirp.html'
    # can input the body of the post
    fields = ['body']

    # makes it so that the user who makes the chirp is the author of the chirp
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ChirpDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_chirp.html'
    # success_url = reverse_lazy('posts:home')

    # makes sure the author of the post is the only one who can delete it
    def test_func(self):
        chirp = self.get_object
        return self.request.user == chirp.username