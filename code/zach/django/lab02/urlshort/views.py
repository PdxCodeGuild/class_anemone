import random
import string
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UrlForm
from .models import UrlData

# Create your views here.

def home_page_view(request):
    return render(request, "base.html")

def url_short(request):
    # model = UrlData
    # f = UrlForm
    if request.method == 'POST':
        f = UrlForm(request.POST)
        
        if f.is_valid():
            slug = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
            url = f.cleaned_data['url']
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            f = UrlForm()
            data = UrlData.objects.all()

            context = {
                'f': f,
                'data': data,
            }
            return render(request, 'urlshort/url.html',context)
    else:
        f = UrlForm()
        data = UrlData.objects.all()   
    
        context = {
            'f' : f,
            'data': data,
        }
    return render(request, 'urlshort/url.html', context)

def url_Redirect(request, slug):
    r = get_object_or_404(UrlData, slug=slug)
    return HttpResponseRedirect(r.url)