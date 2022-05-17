'''
Class Anemone
Lab 15
Bailey Baker
'''

import requests

while True:
    # initializing variables
    page = 1
    next_page =''

    # input to quit program or enter keyword to be found
    keyword = input('Enter a keyword or enter "exit" to quit: ').lower()

    # if statement to break loop if 'exit' is entered instead of a keyword
    if keyword == 'exit':
        break

    # loop for selected keyword 
    while next_page != 'done':
        
        # get response from fav quotes with correct page and keyword as paramaters
        response = requests.get('https://favqs.com/api/quotes', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Accept': 'application/json'}, params = {'filter': keyword, 'page': page})
        
        # parse to json format and get value for all quotes for page
        quotes = response.json()['quotes']
        # counter for showing number of quotes per page
        counter = 0

        # loop to get amount of quotes contained on page
        for quote in quotes:
            counter += 1

        print(f"{counter} quotes associated with nature - page {page}")

        #prints each quote on the page with their respective author
        for quote in quotes:
            print(f"""
            {quote['author']}: {quote['body']}
            """)
        
        #user input to determine if new keyword or next page for same keyword
        next_page = input("enter 'next page' or 'done': ").lower()

        if next_page == 'next page':
            page += 1
            continue

    
