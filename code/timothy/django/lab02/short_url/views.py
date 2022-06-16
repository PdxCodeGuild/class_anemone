from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from random import choice
from string import ascii_letters, digits

from short_url.models import ShortURL

def index(request):
    return HttpResponse('Good to Go')

def random_chars(request):
    chars = ascii_letters + digits
    randchars = "".join([choice(chars) for _ in range(6)])
    return randchars

def random_url(request):
    new_url = random_chars()
    if ShortURL.objects.filter(short_url=new_url).exists():
        return random_url(request)
    return new_url