from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import UrlShortener
import random
import string

def index(request):
    if request.method == 'GET':
        context = {
            'url_list' : UrlShortener.objects.all(),
        }
        return render(request, 'index.html', context)
    else:
        url = request.POST['url'] 
        # randomly generate a code using ASCII leters and numbers
        characters = string.ascii_letters + string.digits
        short = []

        # appened each new character to a list named short
        while len(short) < 10:
            short.append(random.choice(characters))

        #convert list into string
        code = ''.join(short)

        #create new object using newly generated string and given URL
        UrlShortener.objects.create(url=url, code=code)

        context = {
            'url_list' : UrlShortener.objects.all(),
        }
        return render(request, 'index.html', context)

def redirect(request, code):
    redirect = get_object_or_404(UrlShortener, code=code)

    return HttpResponseRedirect(redirect.url)