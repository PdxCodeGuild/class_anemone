#Lab15: Quotes API

import requests
import pprint

#Version1: Get a randon quote
response = requests.get('https://favqs.com/api/qotd', headers = {'accept' : 'application.json'})
data = response.json()

quote_data = data['quote']

author = quote_data['author']
quote = quote_data['body']

#print(f'"{quote}" - {author}')

#Version2: List quotes by keyword
keyword = input("Enter a keyword to search for a quote: ")
page = 1

while True:
    k_response = requests.get('https://favqs.com/api/quotes', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = {'filter' : keyword, 'page' : page})
    k_data = k_response.json()
    k_quote_data = k_data['quotes']

    current_page = k_data['page']

    print(f'\n\n{len(k_quote_data)} quotes associated with {keyword} - page {current_page}')
    #pprint.pprint(k_data)

    while True:
        #print quote and author
        for item in k_quote_data:
            k_author = item['author']
            k_quote = item['body']
            print (f'"{k_quote}" - {k_author}\n')
        break


    #Allow user to navigate to next page or quit
    page_option = input('Enter "next page" or "done: ')
    if page_option == "next page":
        page += 1
    elif page_option == "done":
        break

    