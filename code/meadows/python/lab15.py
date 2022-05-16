import requests
import pprint
import json

#-------------------------------------------------# VERSION 2 #---------------------------------------------------------#

# keywords = keyword
# page = 1

# while True:
page = int(input('enter a page number: '))
keyword = input('Enter a keyword for a Quote: ')

response = requests.get('https://favqs.com/api/quotes', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Accept': 'application/json'}, params = {'filter': keyword, 'page': page})

data = response.json()
# body = quote['quote']['body']
    # author = quote['author']
    # pages = quote['page']


   
# pprint.pprint(quote)
    

for x in data['quotes']:
    print(x['body'])
