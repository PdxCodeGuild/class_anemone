' Lab 15 - Quotes API '

import requests

' ~~ Version 1 ~~ '

# response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token = "855df50978dc9afd6bf86579913c9f8b"'})
# dict = response.json()
# quote = (f"\"{dict['quote']['body']}\" -{dict['quote']['author']}")
# print(quote)

' ~~ Version 2 ~~ '

while True:

    # resets page num to 1 for each new keyboard
    page = 1
    keyword = input("Enter a keyword to find related quotes, or 'X' to exit this program: ").lower()

    # allows user to quit program
    if keyword == 'x':
        break
    else:
        while True:

            # request list of quotes from website and convert to list of dicts
            response = requests.get('https://favqs.com/api/quotes/', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = {'page': page, 'filter': keyword})
            dict = response.json()
            quotes = dict['quotes']

            # turn list of dicts into pretty strings
            for quote in quotes:
                body = quote['body']
                author = quote['author']
                print(f"\n\"{body}\" -{author}\n")
            
            # give user the option to see another page of quotes or return to keyword search
            page_quit = input("Enter 'next page', or 'quit' to return to keyword search: ").lower()
            if page_quit == 'next page':
                page += 1
            elif page_quit == 'quit':
                break
