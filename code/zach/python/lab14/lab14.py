import requests

def get_dad_joke():
    r = requests.get('https://icanhazdadjoke.com/', headers = {'Accept': 'application/json'})
    data = r.json()
    print(data['joke'])


get_dad_joke()