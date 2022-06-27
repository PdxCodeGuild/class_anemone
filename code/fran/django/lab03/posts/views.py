from django.views.generic import ListView, DetailView

from .models import Post
      
class ChirpListView(ListView):  
    model = Post
    template_name = 'home.html'

class ChirpDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

