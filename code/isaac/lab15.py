'''Quotes API'''
import pprint
import requests

# create a variable containing the request for the api
# response = requests.get('https://favqs.com/api/qotd', headers={'Content-Type': 'application/json'})

# print(response.json()['quote'])
while True:
    user_input = input("Enter your search word: ")
    page = 1
    while True:

    # Access the favqs API
        api = requests.get('https://favqs.com/api/quotes', headers={'Authorization': 'Token token="cda8804982a486346d86371faa09cae7"'}, params={'filter': user_input, 'page': page})

    # pprint.pprint(api.json())
        print(f"Page {page}")
        # create REPL
        for quote in api.json()['quotes']:
            print(f"{quote['body']} - {quote['author']}\n")
        
        user_page = input("Enter 'next page' for next page or enter 'done' to exit.\n")
        if user_page == 'done':
            break
        else:
            page += 1


