from pprint import pprint
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Urlshort
from .paw import Paw2

paw = Paw2()

def index(request):
    urls = Urlshort.objects.all().order_by('-num_clicked')
    context = {'urls':urls}
    return render(request, 'urlshortener/index.html', context)

def newurl(request):
    surl = paw.gen()
    nsurl = paw.redo(surl)
    Urlshort.objects.create(ourl=request.POST['ourl'], surl=nsurl)
    return HttpResponseRedirect(reverse('urlshortener:index'))

def direct(request, kurl):
    try:
        urls = Urlshort.objects.all()
        print(urls)
        for url in urls:
            k=url.surl
            if url.surl == kurl:
                naddress = url.ourl
                
    except: 
        return HttpResponseRedirect(reverse('urlshortener:index'))
    else:
        url.num_clicked += 1
        url.save()
        return HttpResponseRedirect(str(naddress))
# Create your views here.
