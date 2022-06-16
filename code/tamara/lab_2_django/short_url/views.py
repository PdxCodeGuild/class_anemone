from django.shortcuts import render
from .models import ShortUrl
import random, string

def index(request):
    # url item is a list of the codes and their urls
    # still need to figure out how to make the code randomly generated
    # url needs to be user input
    url_items = ShortUrl.objects.all()
    return render(request, 'short_url/index.html', url_items)

def code(request, pk):
    url_characters = string.ascii_letters + string.digits
    
