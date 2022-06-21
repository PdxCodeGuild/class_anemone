from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Urlshort
from .paw import Paw2

paw = Paw2()

def index(request):
    urls = Urlshort.objects.order_by('num_clicked')
    url_list = {
        'urls': urls
    }
    print(Urlshort.objects.order_by('num_clicked'))
    return render(request, 'urlshortener/index.html', url_list)

def newurl(request):
    print(request.POST)
    surl = paw.gen()
    nsurl = paw.redo(surl)
    Urlshort.objects.create(ourl=request.POST['ourl'], surl=nsurl)
    return HttpResponseRedirect(reverse('urlshortener:index'))

def redirect(request, surl_id):
    naddress = get_object_or_404(Urlshort, pk=request.POST[''])

# Create your views here.
