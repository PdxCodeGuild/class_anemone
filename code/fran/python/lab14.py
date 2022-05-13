# Lab14 - Dad Joke API
# Fran Kappes

import pprint

import requests

# Make API request 
response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'}, params={'appID': 'D065A', 'routes': 70})

# Display joke to user
print(response.json()['joke'])

