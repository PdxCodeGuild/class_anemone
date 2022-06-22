from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Urlshort
from .paw import Paw2

paw = Paw2()

def index(request):
    urls = Urlshort.objects.order_by('num_clicked')
    stupid = {
        'urls': urls
    }
    for x in Urlshort.objects.order_by('num_clicked'):
        print(x.ourl, x.surl, x.num_clicked)
    return render(request, 'urlshortener/index.html', stupid)

def newurl(request):
    print(request.POST)
    surl = paw.gen()
    nsurl = paw.redo(surl)
    Urlshort.objects.create(ourl=request.POST['ourl'], surl=nsurl)
    return HttpResponseRedirect(reverse('urlshortener:index'))

def redirect(request):
    naddress = get_object_or_404(Urlshort, pk=request.POST[''])

# Create your views here.
