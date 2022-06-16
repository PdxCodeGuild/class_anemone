from django.http import HttpResponse
from django.http import HttpReponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Affirmative")