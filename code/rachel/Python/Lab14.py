#Lab14: Dad Joke API

import pprint
import requests

#send HTTP request to icanhazdadjoke.com
response = requests.get('https://icanhazdadjoke.com/', headers = {'accept': 'application/json'})
#turn into dictionary
data = response.json()

#get joke out of dictionary and show to user
joke = data['joke']

print(joke)