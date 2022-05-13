from urllib import response
'''Dad Joke API'''
# import modules for use
# random module to use for random seconds per joke
# requests to request information from URL
# time for time between jokes
import random
import requests
import time

# response variable for the url with headers as 'Accept': 'application/json'
response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
time.sleep(1)  # one second sleep between jokes
print(response.json()['joke'])  # print off the joke to the user