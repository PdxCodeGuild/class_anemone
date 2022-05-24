import json
import requests
import pprint



next = True

while next == True:
    
    keyword = input("Enter a keyword you would like to look for in a quote or 'done' to quit. ").lower()
        
    if keyword == 'done':
        next = False
        break
        
    key = True
    
    while key == True:

        for i in range (1, 25, 1):              # problem was that it was iterating throught the first page twice cause it started at 0 defaulted to 1 then went to 1 on next page and returned 1 again
            response = requests.get(f'https://favqs.com/api/quotes?page={i}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Accept': 'application/json'})
            quote = response.json()
                           
            for x in range(0, 25, 1):
                body = quote['quotes'][x]['body']
                author = quote['quotes'][x]['author']
                cacacacacombo = f'\n {x} Quote : {body} \n {x} Author : {author} '
                pprint.pprint(cacacacacombo)
            
            
            user = input('enter next page or done to return to keyword: ').lower()
                        
            if user == 'next page':
                key = True
            elif user == 'done':
                key = False
                break
            else:
                key = False
                print('Your input was not recognized returning to keyword.')
                break
                







