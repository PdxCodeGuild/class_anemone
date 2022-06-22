from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from string import ascii_letters, digits
import random

from .models import ShortUrl

def index(request):
    return render(request,'short_url/index.html')

def createurl(request):
    short = ShortUrl()
    if request.method == 'POST':
        short.small_url = ''.join(random.choice(ascii_letters+digits) for x in range(8))
        short.long_url = request.POST["long_url"]
        new_url = ShortUrl(long_url=short.long_url, small_url=short.small_url)
        new_url.save()

        return HttpResponseRedirect(request, 'short_url:index.html', {'short':short})
