from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from .models import UrlChoppa
from django.utils import timezone

import random
import string

def code_six():
    letters = string.ascii_letters
    digits = string.digits
    all_characters = letters + digits 
    pass_length = 6
    password = []
    pass_length = float(pass_length)
    while len(password) < pass_length:
        password.append(random.choice(all_characters))
    code = (''.join(password))   
    return code

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        url_submit = request.POST['url']
        print(url_submit)
        code = code_six()
        u = UrlChoppa(url=url_submit,pub_date=timezone.now(),url_code=code,ip_addy='')
        u.save()
        context = {'url_chopped':UrlChoppa.objects.all()}
    else: 
        context = {'url_chopped':UrlChoppa.objects.all()}  
      
    return render(request,'choppa/index.html', context)


def remove(request):
    id = request.POST['remove']
    u = UrlChoppa.objects.get(pk=id)    
    u.delete()
    return HttpResponseRedirect (reverse("choppa:index"))

def redirect(request,url_code): # gained a little bit of inspiration from Timothy
    url_code = get_object_or_404(UrlChoppa, url_code=url_code)
    return HttpResponseRedirect (url_code.url)
