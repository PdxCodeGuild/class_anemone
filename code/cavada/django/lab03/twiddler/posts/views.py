from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Twiddle

# Create your views here.
 
class TwiddleListView(ListView):
    model = Twiddle
    template_name = 'landing.html'
    def get_queryset(self):
        return Twiddle.objects.order_by('-created_date')    

class TwiddleDetailView(DetailView):
    model = Twiddle
    template_name = 'twiddle_detail.html'

class TwiddleCreateView(LoginRequiredMixin, CreateView):
    model = Twiddle
    template_name = 'twiddle_new.html'
    fields = ['twidd', 'twiddle']

    def form_valid(self, form):
        form.instance.twiddler = self.request.user
        return super().form_valid(form)

class TwiddleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Twiddle
    template_name = 'twiddle_edit.html'
    fields = ['twidd', 'twiddle']

    def test_func(self):
        twiddle = self.get_object()
        return self.request.user == twiddle.twiddler

class TwiddleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Twiddle
    template_name = 'twiddle_delete.html'
    success_url = reverse_lazy('posts:landing')

    def test_func(self):
        twiddle = self.get_object()
        return self.request.user == twiddle.twiddler