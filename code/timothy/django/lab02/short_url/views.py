from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import URLShortener
from random import choice
from string import ascii_letters, digits

def index(request):
    taken_url = get_object_or_404(URLShortener)
    given_url = get_object_or_404(URLShortener)
    context = {
       'taken_url': taken_url,
       'given_url': given_url,
    }
    return render(request, 'short_url/index,html', context)

def randomgen():
    chars = ascii_letters + digits
    x = ''.join([choice(chars) for _ in range(6)])
    return x

def randomurl(model_instance):
    random_url = randomgen()
    model_class = model_instance.__class__

    if model_class.objects.filter(given_url=random_url).exists():
        return random_url(model_instance)
        
    return random_url
