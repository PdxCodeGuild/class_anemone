# Lab15 - Quotes API
# Fran Kappes

import requests

import pprint

# Initialize page variable, to be used as a request message element
page_num = 1

while True:
    quote_filter = input("Enter a keyword to search for quotes, or 'exit': ")

    if quote_filter.lower() in ('exit','quit','done','q',''):
        break
    else:
        while True:
            # Make API request
            # response = requests.get('https://favqs.com/api/qotd', headers={'Accept': 'application/json'})   # Version 1
            response = requests.get('https://favqs.com/api/quotes', headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Accept': 'application/json'}, params={'filter': quote_filter, 'page': page_num})

            # pprint.pprint(response.json())   ### Determine response message data elements
    
            results = response.json()['quotes']     # list of dictionaries

            # Display quotes to user
            for result in results:
                print('')
                print(result['body'],'  -',result['author']) 
                print('')

            next_page = input(f"Enter 'next page' or 'done': ")

            if next_page.lower() in ('next page','next','n'):
                page_num += 1
                continue
            elif next_page.lower() in ('done','exit','quit','q'):
                break
            else:
                break
        