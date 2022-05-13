# ....Lab 14 Version 1 ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

import requests
import pprint
import time

def random_dad_joke():
    response = requests.get("https://icanhazdadjoke.com", headers={'Accept':'application/json'})
    response_dict = response.json()
    joke = response_dict['joke']
    print("Here's a random Dad Joke")
    time.sleep(3)
    print(joke)

# random_dad_joke()

# ....Lab 14 Version 2 ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

def search_dad_jokes():
    search_term = input('Enter a keyword and I will tell you some Dad Jokes: ')
    response = requests.get('https://icanhazdadjoke.com/search', headers ={'Accept':'application/json'}, params={'term':search_term})
    response_dict = response.json()
    jokes = response_dict['results']
    for joke in jokes:
        print(joke['joke'])
        time.sleep(5)
search_dad_jokes()



