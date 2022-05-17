# response = requests.get("https://developer.trimet.org/ws/v2/vehicles", params={'appID': 'D065A3A5DAE4622752786CEB9', 'routes': 70"})
import time
import json
import pprint
import requests
x = 0
while x < 10:
    x += 1
    page = 1
    search = input("\nsearch for quotes by keyword?? ")
    keyword = input('keyword: ')
    while search != 'n': # while user wants to search, it will continue
        page_filt = f"page={x}&" #used this to modify page number, but also permit taking out that paramater in the url
        url = f'https://favqs.com/api/quotes/?{page_filt}filter={keyword}'
        print(f"{url} \tpage: {page}") #keep an account of url and page requested
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get(url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        resp = response.json()
        quotes = resp['quotes'] 
        print(f"{len(quotes)} quotes associated with {keyword}\n") # give number of quotes associated with keyword per page
        print("Pick from list of authors: 'enter corresponding digit' ") # gives user option to select quote by author
        page +=1
        authors = {}
        for i , quote in enumerate(quotes): # creatinga  dictionary list to breakout author choice by integer
            auth = {}
            # print(quote['author'])
            auth = {i:quote['author']}
            author_a = quote['author']
            authors.update(auth)
        auth_list = []
        for i, auth in enumerate(authors): # display of authors for user selection
            print(f"{i} - {authors[auth]} -")
            # print(f"\t({i}) {authors[i]}")
            auth
        # pprint.pprint(quotes)  
        choice = input(f"\nenter corresponding #\n\t(or 'a' for all quotes in page {page}) ") # gives option to see all quotes
        if choice != 'a':
            a = authors[int(choice)]
            x+=1  
        
            for quote in quotes:
                if quote['author'] == a:
                    # pprint.pprint('\n\t',quote['body'],'\n\n\t-',a,'\n')
                    print(f"\n\t{quote['body']}\n\n\t -{a}\n\n") # displays the quote of user's choice
                    time.sleep(1)
        else:
            for i, quote in enumerate(quotes):
                print(f"{i}: {quote['body']} \n\t-{quote['author']}\n") # spits out all quotes at slowed down speed
                # print(f"\n\t{quote['body']}\n\n\t -{a}\n")
                time.sleep(.1)

        if quote['body'] == 'No quotes found': # if no quotes found, it resets loop
            break
                # time.sleep(1)
        elif resp['last_page']==True: # if no more pages resets loop, since we can't access any other pages, so no reason to ask
            # (resp['last_page'])
            print('No other pages to search...')
            break
        else:
            print('there are more pages to search...')
            search = input(f"\tenter to next page ({page})? ") # give option for user to quit essentially, ensures appropriate conintance of while loop
