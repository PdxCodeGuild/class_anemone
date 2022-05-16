import time
import requests
import json
import pprint




response = requests.get('https://icanhazdadjoke.com/search', headers = {'accept': 'application/json'})
# print(response.json())
joke = response.json()

pprint.pprint(joke)
