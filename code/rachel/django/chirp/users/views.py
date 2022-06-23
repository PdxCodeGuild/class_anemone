from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class SignUpPage(CreateView):
    form = UserCreationForm
    view_name = 'signup.html'
    success_url = reverse_lazy('login')

class ProfilePage(DetailView):
    model = User
    view_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

def profile(request, username):
    profile = get_object_or_404(User, username=username)
    context = {
        'profile' : profile
    }
    return render(request, 'profile.html', context)


