

import requests
import pprint


##get a Random Quote
##Version 1


# response = requests.get("https://favqs.com/api/qotd", headers = {"accept": "application/json"})
# ##raw data
# # print(response.text)

# ## turn into python dict json()
# data = response.json()
# quote = data['quote']
# # print(quote)

# ##prints author
# author = quote['author']
# print(author)
# ##prints body of the quote
# body = quote['body']
# print(body)


##List quotes by keyword
##Version 2




# #next-page
# next_page = ''

## While loop for user to enter keyword until done
while True:

    ##pagination
    page = 1


    user_keyword = input("Please enter a keyword that you would like to search for or 'quit': ")
    while True:
            
        response = requests.get("https://favqs.com/api/quotes", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},params= {'filter': user_keyword,'page':page})
        # print(response.text)
        # url = "https://favqs.com/api/quote"
        # response = requests.get(url,headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        result = response.json()['quotes']
        # pprint.pprint(result)

        ## response codes
        
        for quote in result:
            author = quote['author']
            tagline = quote['tags']
            body = quote['body']
            print(author,tagline,body)

        quit = input("Would you like to 'quit' or 'next page'? ")

        if quit == 'quit':
            break
        elif quit == 'next page':
            page += 1
            continue

        # if user_keyword == 'quit':
        #     break

        # if user_keyword == 'next page':
        #     page += 1

