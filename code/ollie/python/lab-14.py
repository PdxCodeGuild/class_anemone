' Lab 14 - Dad Joke API '

import requests

response = requests.get("https://icanhazdadjoke.com/", headers = {"accept": "application/json"})         # request joke from website given url, add headers
joke = response.json()                          # turn icky response into a dictionary
print(joke['joke'])                             # print joke for user