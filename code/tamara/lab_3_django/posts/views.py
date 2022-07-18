from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post

# for listing out the chirps on the homepage
class ChirpListView(ListView):
    model = Post 
    template_name = 'home.html'

    ##### V is this necessary? shouldnt they already be ordered this way?
    def get_queryset(self):
        return Post.objects.order_by('-created')

# class ChirpDetailView(DetailView):
#     model = Post 
#     template_name = 'post_detail.html'

class ChirpCreateView (LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_chirp.html'
    # can input the body of the post
    fields = ['body']
    success_url = reverse_lazy('posts:home')

    # makes it so that the user who makes the chirp is the author of the chirp
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_chirp.html'
    success_url = reverse_lazy('posts:home')

    # makes sure the author of the post is the only one who can delete it
    def test_func(self):
        chirp = self.get_object()
        return self.request.user == chirp.author