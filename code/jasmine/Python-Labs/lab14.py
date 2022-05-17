
## Dad Joke API


import requests


response = requests.get("https://icanhazdadjoke.com/", headers = {"accept": "application/json"})
print(response.text)

data = response.json()
print(data)

joke = data['joke']

print(joke)