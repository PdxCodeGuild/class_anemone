from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Urlshort
from paw import Paw2

def index(request):
    urls = Urlshort.objects.all()
    urllist = {
        'urls':urls
    }
    return render(request, 'urlshortener/index.html', urllist)

def newurl(request, input):
    surl = Paw2.gen()
    nsurl = Paw2.redo(surl)
    Urlshort.objects.create(ourl=input, surl=nsurl)
    return HttpResponseRedirect(reverse('urlshortener:index'))

def redirect(request, surl_id):
        naddress = get_object_or_404(Urlshort, pk=request.POST[''])

# Create your views here.
