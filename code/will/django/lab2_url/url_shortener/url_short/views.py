import re
from django.shortcuts import render, redirect
import random
from .models import Url
import string

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('you are at the index')

def urls(request):
    if request.method =='POST':
        length = 10
        random_url = ''.join(random.sample(string.ascii_letters+string.digits,length))
        input_url = request.POST['url']
        
                
    return HttpResponse('you are at the' )