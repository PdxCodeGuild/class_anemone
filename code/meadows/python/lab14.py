import time
import requests
import json
import pprint




response = requests.get("https://icanhazdadjoke.com/", headers = {'Accept': 'application/json'})

joke = response.json()
laugh = joke['joke']
print(f'\n{laugh}\n')

# can also do pprint.pprint() to see all the jokes in respone.json()