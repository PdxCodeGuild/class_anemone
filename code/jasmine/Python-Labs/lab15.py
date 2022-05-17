

import requests


# ## get a Random Quote
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

## While loop for user to enter keyword until done
while True:

    user_keyword = input("Please enter a keyword that you would like to search for or 'quit': ")

    url = "https://favqs.com/api/quotes?page=<page>&filter={user_keyword}"
    new_response = requests.get(url,headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    result = new_response.json()
    print(result)

    if user_keyword == 'quit':
        break

    test = []

    # for i in result:
    #     new_quotes = i['body']
    #     test.append(new_quotes)
    # print(test)
