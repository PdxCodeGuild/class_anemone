from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from random import choice
from string import ascii_letters, digits

from short_url.models import ShortURL

def index(request):
    return render(request, 'short_url/index.html')

def random_chars(request):
    chars = ascii_letters + digits
    randchars = "".join([choice(chars) for _ in range(6)])
    return randchars

def random_url(long_url):
    new_url = random_chars()
    if ShortURL.objects.filter(short_url=new_url).exists():
        return random_url(long_url)
    return new_url

def shorten(request):
    ShortURL(long_url = request.POST['long_url']).save()
    random_url()
    ShortURL(short_url = request.POST['short_url']).save()
    return HttpResponseRedirect(reverse('short_url:index'))
