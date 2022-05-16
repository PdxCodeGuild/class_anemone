import requests
import pprint
import json



response = requests.get('https://favqs.com/api/qotd', headers = {'Accept' : 'application/json'})

quote = response.json()
body = quote['quote']['body']
author = quote['quote']['author']
print(f'\nAuthor: {author}\n\nQuote: {body}\n')



# headers = {'Accept': 'application/json'}

# response = requests.get("https://icanhazdadjoke.com/", headers = {'Accept': 'application/json'})


# joke = response.json()
# print('\n')
# pprint.pprint(joke)
# print('\n')