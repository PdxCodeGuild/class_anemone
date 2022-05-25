import requests
import json

search_term = input("Please enter a keyword for your quote search")
page = 0
response = requests.get('https://favqs.com/api/quotes?page=<page>&filter=<keyword>',
 params= {'filter':search_term, 'page' : page },
  headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
quote_response = json.loads(response.text)
page = quote_response['page']
print_output = quote_response['quotes']

for quote in print_output:
    author = quote['author']
    quote = quote['body']
    print(f'{quote} - {author}')
