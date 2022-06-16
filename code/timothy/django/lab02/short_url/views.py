from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import URLShortener
from random import choice
from string import ascii_letters, digits

def index(request):
    taken_url = get_object_or_404(URLShortener, pk=pk)
    given_url = get_object_or_404(URLShortener, pk=pk)
    context = {
       'taken_url': taken_url,
       'given_url': given_url,
    }
    return render(request, 'short_url/index,html', context)

def randomgen():
    chars = ascii_letters + digits
    x = ''.join([choice(chars) for _ in range(6)])
    return x

def randomurl(exist_check):
    random_url = randomgen()
    model_class = exist_check.__class__

    if model_class.objects.filter(given_url=random_url).exists():
        return random_url(exist_check)

    return random_url
