
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests


import json
from .forms import *


# Create your views here.
def zillow(request):
    address = request.POST["address"]
    city = request.POST["city"]
    state = request.POST["state"] 
    zip = request.POST["zip"]
    print(request.POST)
    stored_data = []
     
    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

    querystring = {"location":f'{address}. {city},{state}. {zip}'}

    headers = {
	"X-RapidAPI-Key": "a734b12ec8msh6f0fe8ed4e1ba42p170be5jsn34eb295dbddb",
	"X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
}

    response = requests.request("GET", url, headers=headers, params=querystring)

    zpid = response.json()
    print(type(dict(zpid)))


    url = "https://zillow-com1.p.rapidapi.com/property"

    querystring2 = {"zpid":f'{zpid["zpid"]}'}

    headers2 = {
	"X-RapidAPI-Key": "a734b12ec8msh6f0fe8ed4e1ba42p170be5jsn34eb295dbddb",
	"X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
}

    response2 = requests.request("GET", url, headers=headers2, params=querystring2)

    parse_json = json.loads(response2.text)
    print(parse_json)
  

#     response = requests.request("GET", url, headers=headers, params=querystring)
#     stored_data.append(response)
#     parse_json = json.loads(response.text)
#     display_data = parse_json.keys()
#     # print(display_data)
#     print(parse_json)

  

    weather_url = "https://visual-crossing-weather.p.rapidapi.com/history"

    weather_querystring = {"startDateTime":"2019-01-01T00:00:00","aggregateHours":"24","location":f'{address}. {city},{state}. {zip}',"endDateTime":"2019-01-03T00:00:00","unitGroup":"us","dayStartTime":"8:00:00","contentType":"json","dayEndTime":"17:00:00","shortColumnNames":"true"}


    
    weather_headers = {
	"X-RapidAPI-Key": "a734b12ec8msh6f0fe8ed4e1ba42p170be5jsn34eb295dbddb",
	"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
}

    weather_response = requests.request("GET", weather_url, headers=weather_headers, params=weather_querystring)
    weather_json = json.loads(weather_response.text)
    weather_data = weather_response.json()
    # print(weather_data)
    wdir = weather_json['locations'][f'{address}. {city},{state}. {zip}']['values'][0]['wdir']
    temp = weather_json['locations'][f'{address}. {city},{state}. {zip}']['values'][0]['temp']  
    maxt = weather_json['locations'][f'{address}. {city},{state}. {zip}']['values'][0]['maxt']
    visibility = weather_json['locations'][f'{address}. {city},{state}. {zip}']['values'][0]['visibility']
    wspd = weather_json['locations'][f'{address}. {city},{state}. {zip}']['values'][0]['wspd']
    solarenergy = weather_json['locations'][f'{address}. {city},{state}. {zip}']['values'][0]['solarenergy']
    cloudcover = weather_json['locations'][f'{address}. {city},{state}. {zip}']['values'][0]['cloudcover']
    mint = weather_json['locations'][f'{address}. {city},{state}. {zip}']['values'][0]['mint']

# image':image, 'zipcode':zipcode, 'description':description,'home_type':home_type, 'living_area':living_area, 'hoa':hoa,'address': address, 'bathrooms': bathrooms, 'bedrooms':bedrooms, 'lot_size':lot_size, 'rent_zestimate':rent_zestimate

    address = parse_json['address']['streetAddress']
    zipcode = parse_json['zipcode']
    description = parse_json['description']
    home_type = parse_json['homeType']
    living_area = parse_json['livingArea']
    # hoa = parse_json['monthlyHoaFee']
    image = parse_json['imgSrc']

    bathrooms = parse_json['bathrooms']
    bedrooms = parse_json['bedrooms']
    last_price = parse_json['price']
    lot_size = parse_json['resoFacts']['lotSize']
    # zestimate = parse_json['zestimate']
    rent_zestimate = parse_json['rentZestimate']

    context = { 'last_price':last_price,'image':image, 'zipcode':zipcode, 'description':description,'home_type':home_type, 'living_area':living_area,'address': address, 'bathrooms': bathrooms, 'bedrooms':bedrooms, 'lot_size':lot_size, 'rent_zestimate':rent_zestimate, 'wdir':wdir, 'maxt':maxt, 'visiblity':visibility, 'wspd':wspd, 'solarenergy':solarenergy, 'cloudcover':cloudcover, 'mint':mint, 'temp':temp, 'weather_response':weather_json }

    return render (request,'users.html', context)

   



def new(request):
    form = InputForm()
    return render(request, 'new.html', {"form":form })