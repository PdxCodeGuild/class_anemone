from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Chirp

class ChirpListView(ListView):
    model = Chirp
    template_name = 'home.html'

    def get_queryset(self):
        return Chirp.objects.order_by('-created')

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'post_detail.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.chirpname = self.request.user
        return super().form_valid(form)

class ChirpEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chirp
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.chirpname

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = 'post_delete.html'
    success_url = reverse_lazy('chirp:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.chirpname