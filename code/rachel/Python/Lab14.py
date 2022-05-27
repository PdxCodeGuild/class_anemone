#Lab14: Dad Joke API

import pprint
import requests

#send HTTP request to icanhazdadjoke.com
user_search = input("Enter key word to search for a joke: ")
response = requests.get('https://icanhazdadjoke.com/', headers = {'accept' : 'application/json'})
search = requests.get('https://icanhazdadjoke.com/search', headers = {'accept' : 'application/json'}, params = {'term' : user_search})


#turn into dictionary
data = response.json()
search_data = search.json()

#get joke out of dictionary and show to user
joke = data['joke']
#print(joke)
results = search_data['results']
pprint.pprint(results)