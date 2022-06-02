import requests
import pprint
import json

#-------------------------------------------------# VERSION 2 #---------------------------------------------------------#
new = True
lines = '----------------------------------------'        # used for splitting info to be more easy on the eyes to read qoute / pages and so on
page = 1

while new:

    keyword = input('\nEnter a keyword for a Quote or "DONE" to stop: ')

    if 'done' in keyword:
        print('\nBYE!!!\n')
        break
    
    while True:
                                    # response is getting the api fomr the website to use , then using the header to authorize.. NEED a key unless you are doing the Qotd and then using Params as key works for the adress search bar (manipulates it)
        response = requests.get('https://favqs.com/api/quotes', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Accept': 'application/json'}, params = {'filter': keyword, 'page': page})

        data = response.json()  # turning our response statement into a jason file to be read and used in python

        k_word = []    # used to get the length of how many quotes are in the key word input

        for x in data['quotes']:     #taking the data and adding the key ['qoutes'] as its the first itteration of the dict then using x in for to get the value in the qoutes as the body ( the actual qoute )
            every = x['body']     # this one to get rid of the list look and look more clean
            body = x['body']
            body = body.split('[.]')  # body was used to split the qoutes by . then append it to k_word to have a list of list to get the length of how many qoutes there truly are
            k_word.append(body)
            
        print(f'\n{lines}')
        print(f'\n{len(k_word)} Quotes {k_word} - page {page}\n') # len(k_word) is explained in # above but placed in here to give the length to the user with their word of choice and the page number it is on and keep track
        print(f'\n{every}\n')  # for the actual quote for the user
        print(f'{lines}\n')
                                # used line to seperate the info from everything to make it easier to see
    

        pages = input('\nEnter "Next" for next page OR "Done" to finish: \n').lower() 

        if 'next' in pages:
            page += 1                # next page changes the page giving a new qoute from the keyword 
            continue

        elif 'done' in pages:
            print(f"\nReturning you to the VOID!!!\n")
            break

        else:
            print(f'\n{pages} was not a correct response.. TERMINATING!')
            break