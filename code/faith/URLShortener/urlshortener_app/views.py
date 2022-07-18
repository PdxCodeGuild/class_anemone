from secrets import choice
from string import ascii_letters, digits
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import URLShort
from random import choice
from string import ascii_letters, digits

# Create your views here.
from django.http import HttpResponse

def submit():
    return ''.join([choice(ascii_letters + digits) for _ in range(4)])

def index(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_url = submit()
        URLShort.objects.create(long_url=long_url, short_url=short_url)
        context = {
            'final_url': URLShort.objects.all()
        }
        return render(request, 'urlshortener_app/index.html', context)
    else:
        context = {
            'final_url': URLShort.objects.all()
        }
        return render(request, 'urlshortener_app/index.html', context)

def redirect(request, short_url):
    latest_url = get_object_or_404(URLShort, short_url=short_url)
    return HttpResponseRedirect(latest_url.long_url)
