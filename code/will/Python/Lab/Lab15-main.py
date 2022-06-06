import requests
import json
while True:

  search_term = input("Please enter a keyword for your quote search: ")
  page = 0
  response = requests.get('https://favqs.com/api/quotes?page=<page>&filter=<keyword>',
  params= {'filter':search_term, 'page' : page },
  headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
  quote_response = json.loads(response.text)
  page = quote_response['page']
  print_output = quote_response['quotes']

  for quote in print_output:
    quote_output = ''
    author = quote['author']
    quote = quote['body']
    quote_output += F"\n\"{quote} {author} \""
    print(quote_output)
    user_input = input("Press 'n' for the next page or press 'q' to quit: ")
    if user_input == 'n':
      page += 1
    elif user_input == 'q':
      break
