
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
     
    url = "https://zillow56.p.rapidapi.com/search"

    querystring = {"location":f'{address}. {city},{state}. {zip}'}

    headers = {
	"X-RapidAPI-Key": "42123ed4f1msh64988eb134ebadcp1a8ce1jsn4fa401f0b51a",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"

  
}
    
  

    response = requests.request("GET", url, headers=headers, params=querystring)
    stored_data.append(response)
    parse_json = json.loads(response.text)
    display_data = parse_json.keys()
    # print(display_data)
    print(parse_json)

  

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



    address = parse_json['address']['streetAddress']
    zipcode = parse_json['address']['zipcode']
    description = parse_json['description']
    home_type = parse_json['homeType']
    living_area = parse_json['livingArea']
    hoa = parse_json['monthlyHoaFee']
    image = parse_json['hiResImageLink']

    bathrooms = parse_json['bathrooms']
    bedrooms = parse_json['bedrooms']
    last_price = parse_json['lastSoldPrice']
    lot_size = parse_json['lotSize']
    zestimate = parse_json['zestimate']
    rent_zestimate = parse_json['rentZestimate']

    context = {'image':image, 'zipcode':zipcode, 'description':description,'home_type':home_type, 'living_area':living_area, 'hoa':hoa, 'wdir':wdir, 'maxt':maxt, 'visiblity':visibility, 'wspd':wspd, 'solarenergy':solarenergy, 'cloudcover':cloudcover, 'mint':mint, 'temp':temp, 'weather_response':weather_json, 'address': address, 'bathrooms': bathrooms, 'bedrooms':bedrooms, 'last_price': last_price, 'lot_size':lot_size, 'zestimate':zestimate, 'rent_zestimate':rent_zestimate }

    return render (request,'users.html', context)

   

# 'dew': dew, 'temp': temp, 'temp_max': temp_max, 'temp_min' : temp_min, 'precip': precip, 'dew2': dew2, 'humidity' : humidity, 'solarenergy' : solarenergy, 'cloudcover' : cloudcover

def new(request):
    form = InputForm()
    return render(request, 'new.html', {"form":form })