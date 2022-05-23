import requests
import json

response = requests.get('https://icanhazdadjoke.com/search', headers= {'Accept' : 'application/json'})
joke_response = response.text

y = json.loads(joke_response)

for result in y['results']:
    print(result['joke'])




#submission time