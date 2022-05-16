# response = requests.get("https://developer.trimet.org/ws/v2/vehicles", params={'appID': 'D065A3A5DAE4622752786CEB9', 'routes': 70"})

import json
import pprint
import requests

# page
keyword,page = input('keyword: '),int(input('page: '))
url = f'https://favqs.com/api/quotes/?page={page}&filter={keyword}'

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
response = response.json()
response = response['quotes'] 
for i in response:
    print(i['body'])
# pprint.pprint(response)
# pprint.pprint(response.json())
# quote = response['quote']['body']
# author = response['quote']['author']
# print(f"\n{quote} \n \t-{author}")



# { 
#   "user": {
#     "login": "avocado",
#     "password": "FavQsavocado"
#   }
# }

{'author': 'Mortimer Adler',
             'author_permalink': 'mortimer-adler',
             'body': 'One of the embarrassing problems for the early '
                     'nineteenth-century champions of the Christian faith was '
                     'that not one of the first six Presidents of the United '
                     'States was an orthodox Christian.',
             'dialogue': False,
             'downvotes_count': 0,
             'favorites_count': 0,
             'id': 19260,
             'private': False,
             'tags': ['faith'],
             'upvotes_count': 0,
             'url': 'https://favqs.com/quotes/mortimer-adler/19260-one-of-the-em-'}