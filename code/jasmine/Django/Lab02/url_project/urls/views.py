from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


from .models import UrlShortener

import random, string

def index(request):
    if request.method == 'GET':
        context = {
            'url_list': UrlShortener.objects.all(),
        }
        return render(request, 'urls/index.html', context)
    elif request.method == 'POST':
        long_url = request.POST['long-url']
        short_url = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))
        
        UrlShortener.objects.create(long_url=long_url, short_url=short_url)
        context = {
            'url_list':UrlShortener.objects.all(),
        }
        return render(request, 'urls/index.html', context)

def redirect(request, short_url):
    item = get_object_or_404(UrlShortener, short_url=short_url)
    return HttpResponseRedirect(item.long_url)
