from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from random import choice
from string import ascii_letters, digits

from shurl.models import Shurl

def randomizer():
    chars = ascii_letters + digits
    code = "".join([choice(chars) for _ in range(6)])
    return code

def index(request):
    return render(request, 'shurl/index.html')

def shortened(request):
    long_url = request.POST['long_url']
    short_url = randomizer()
    context = {
        'short_url':short_url,
        'long_url':long_url,
    }
    return render(request, 'shurl/shortened.html', context)

