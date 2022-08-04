from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import CustomUser

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(DetailView):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
    
