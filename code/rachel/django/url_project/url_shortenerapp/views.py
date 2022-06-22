from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Store
import random
import string

def index(request):
    if request.method == 'GET':
        context = {
            'url_list' : Store.objects.all(),
        }
        return render(request, 'url_shortenerapp/index.html', context)
    else:
        long_url = request.POST['longurl'] #index.html name attribute
        
        letters = string.ascii_letters
        digits = string.digits
        all_characters = letters + digits

        numbers = []

        while len(numbers) < 6:
            numbers.append(random.choice(all_characters))

        short_url = ''.join(numbers)

        Store.objects.create(long_url=long_url, short_url=short_url)

        context = {
            'url_list' : Store.objects.all(),
        }
        return render(request, 'url_shortenerapp/index.html', context)

def redirect(request, short_url):
    item = get_object_or_404(Store, short_url=short_url)

    return HttpResponseRedirect(item.long_url)


