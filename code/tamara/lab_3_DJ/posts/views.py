from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post

class ChirpListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.order_by('-created')

#### need to figure out how to only get the posts for the author
#### whos username is clicked on
class UserChirpListView(ListView):
    model = Post
    template_name = 'userpage.html'

    def get_queryset(self):
        return Post.objects.order_by('-created')

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_chirp.html'
    fields = 'body' ######

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_chirp.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        chirp = self.get_object()
        return self.request.user == chirp.author

