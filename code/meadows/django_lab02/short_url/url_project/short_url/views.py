from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from string import ascii_letters, digits
from django.utils import timezone
import random

from .models import ShortUrl

def index(request):
    url = ShortUrl.objects.all()
    context = {
        'url':url
    }
    return render(request,'short_url/index.html', context)

def redirect(request, code):
    try:
        urls = ShortUrl.objects.all()
        for url in urls:
            if url.small_url == code:
                new_address = url.long_url             
    except: 
        return HttpResponseRedirect(reverse('short_url:index'))
    else:
        return HttpResponseRedirect(new_address)

def urlsnip(request):
    if request.method == 'POST':
        new = ShortUrl()
        new.long_url = request.POST['long_url']
        new.snipped()
        new.save()
        context = {
            'new':new,
            'url':ShortUrl.objects.all()
        }
        return render(request, 'short_url/index.html', context)

# .order_by('-pub_date')[:1]