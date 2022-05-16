# Lab15 - Quotes API
# Fran Kappes

import requests

import pprint

# Make API request
response = requests.get('https://favqs.com/api/qotd', headers={'Accept': 'application/json'})

# pprint.pprint(response.json())        ### Determine response message data elements
print('')
print(response.json()['quote']['body'],'  -',response.json()['quote']['author']) 
print('')
