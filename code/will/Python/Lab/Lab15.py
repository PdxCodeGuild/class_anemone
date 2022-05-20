import requests
import json

response = requests.get('https://favqs.com/api/qotd',  headers= {'Accept' : 'application/json'})
joke_response = response.text

y = json.loads(joke_response)

print(y)


#submission time