import requests
import json

search_term = input("Please enter a keyword for your quote search")

response = requests.get('https://favqs.com/api/qotd',  headers= {'Accept' : 'application/json'})
joke_response = response.text

y = json.loads(joke_response)

for result in y['results']:
    print(result[search_term])


#submission time