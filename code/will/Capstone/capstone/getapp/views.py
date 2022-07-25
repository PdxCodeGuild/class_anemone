import re
from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib.request
from urllib.request import Request
import json

# Create your views here.
def zillow(request):
     
    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

    querystring = {"location":"santa monica, ca","home_type":"Houses"}

    headers = {
	"X-RapidAPI-Key": "a734b12ec8msh6f0fe8ed4e1ba42p170be5jsn34eb295dbddb",
	"X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
}

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    context = {"response":response.text}
    return render(request,'users.html', context)


def weather(request):
    url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

    querystring = {"aggregateHours":"24","location":"Washington,DC,USA","contentType":"csv","unitGroup":"us","shortColumnNames":"0"}

    headers = {
	"X-RapidAPI-Key": "a734b12ec8msh6f0fe8ed4e1ba42p170be5jsn34eb295dbddb",
	"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    context = {'response':response.text}
    return render (request,'users.html', context)
    
