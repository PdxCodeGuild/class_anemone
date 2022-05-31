import requests
import json


while True:

   
    page = 1
    keyword = input('Enter a keyword to for quotes, or exit: ').lower()

    
    if keyword == 'exit':
        break
    else:
        while True:

            
            quoteoutput = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = {'page': page, 'filter': keyword})
            dict = quoteoutput.json()
            quotes = dict['quote']

           
            for quote in quotes:
                body = quotes['body']
                author = quotes['author']
                print(f"\n\"{body}\" -{author}\n")
            
           
            page_exit = input("Enter 'next page', or 'exit' to return to keyword search: ").lower()
            if page_exit == 'next page':
                page += 1
            elif page_exit == 'exit':
                break

