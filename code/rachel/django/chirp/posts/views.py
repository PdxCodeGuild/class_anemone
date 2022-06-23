from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post

class ChirpListView(ListView):
    model = Post
    view_name = 'home.html'

class ChirpDetailView(DetailView):
    model = Post
    view_name = 'post_detail.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Post
    view_name = 'post_create.html'
    fields = ['author', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    view_name = 'post_edit.html'
    fields = ['author', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    view_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

