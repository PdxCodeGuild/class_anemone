import random, string
from django.shortcuts import render, get_object_or_404
from .models import Url
import string

from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'url_shortener/index.html')


def random_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def Urls(request):
    url = Url.objects.create(url=request.POST['url'], slug=random_code())
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
    return render(request,'url_shortener/redirect.html', {'url':url})

def redirect(request, slug):
    url = get_object_or_404(Url, slug=slug)
    print('!!!!!!!!!!!!!!!!!!!!', url)
    return HttpResponseRedirect(url.slug)


