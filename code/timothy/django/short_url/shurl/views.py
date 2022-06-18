from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Shurl



def index(request):
    context = {}
    return HttpResponse("Working")

def shorten(request, short_url_id):
    short_url = get_object_or_404(Shurl, pk=short_url_id)
    return HttpResponseRedirect(reverse())