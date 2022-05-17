' Lab 15 - Quotes API '

import requests

' ~~ Version 1 ~~ '

response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token = "855df50978dc9afd6bf86579913c9f8b"'})
dict = response.json()
quote = (f"\"{dict['quote']['body']}\" -{dict['quote']['author']}")
print(quote)

' ~~ Version 2 ~~ '

while True:
    keyword = input("Enter a keyword to find quotes related to that word, or 'X' to exit this program: ").lower()
    if keyword == 'x':
        break
    else: 

