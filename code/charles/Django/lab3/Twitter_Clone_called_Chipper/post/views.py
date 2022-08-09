from asyncio.proactor_events import _ProactorSocketTransport
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post



class TwitListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.order_by('-created')

class TwitDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class TwitCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'newpost.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TwitEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class TwitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('Post:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Create your views here.
