from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UrlShort
from django.urls import reverse
import random
import string



# Create your views here.
def random_generator():
    characters = string.ascii_lowercase + string.digits
    empty_string = ''
    while len(empty_string) < 6:
        empty_string += random.choice(characters)
    return empty_string 

def index(request):
    if request.method == 'POST':
        url = request.POST['long_url']
        code = random_generator()
        UrlShort.objects.create(url=url, code=code)
        context = {
            'urls': UrlShort.objects.all()
        }
        return render(request, 'urlshortener/index.html', context)
    else:
        context = {
            'urls': UrlShort.objects.all()
        }
        return render(request, 'urlshortener/index.html', context)

def redirect(request, code):
    search = get_object_or_404(UrlShort, code=code)
    return HttpResponseRedirect(search.url)