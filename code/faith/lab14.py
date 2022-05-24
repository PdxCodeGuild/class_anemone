import pprint
import requests
import json

dadjoke = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})

output = dadjoke.json()
pprint.pprint(output['joke'])

#output = json.loads(dadjoke.text)
#pprint.pprint(output)

