from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortURL
from django.urls import reverse
import uuid

# Create your views here.

def home(request):
    if request.method == 'POST':
        new_url = str(uuid.uuid4())[:6]
        old_url = request.POST['url']
        if len(old_url) <= 5:
            return render(request, 'error.html')
        new_link = ShortURL( new_url=new_url, old_url=old_url)
        new_link.save()
        # return HttpResponse(new_url, {"new_url": new_url, "old_url": old_url})
        context = {"new_url": new_url, "old_url": old_url}
    else:
        context = {}
    return render(request, 'home.html', context)

def short(request, new_url):
    link = get_object_or_404(ShortURL, new_url=new_url)
    return HttpResponseRedirect(link.old_url)