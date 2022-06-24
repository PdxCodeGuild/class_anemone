from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Posts


class HomePageListView(ListView):
    model = Posts
    template_name = "home_page.html"
        
    def get_queryset(self):
        return Posts.objects.order_by('-created')


def newpost(request, user.id):
  


# Create your views here.
