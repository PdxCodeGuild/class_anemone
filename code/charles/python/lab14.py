import requests
import time
import json
import pprint


response = requests.get("https://icanhazdadjoke.com/", headers = {'Accept': 'application/json'})
# response.encoding = 'utf-8'


dad = response.json()
print('\n')
print(dad['joke'])
print('\n')