# Lab14 - Dad Joke API
# Fran Kappes

import requests
import time

while True:
    print('')
    user_action = input("Would you like to hear a joke? (y)es or (n)o: ")

    if user_action.lower() in ('y','yes','yep','ok'):
        print('')
        search_string = input("What kind of joke would you like to hear? Enter a search string: ")
        print('')

        # Make API request 
        #response = requests.get('https://icanhazdadjoke.com', headers={'Accept': 'application/json'})  # Part 1
        response = requests.get('https://icanhazdadjoke.com/search', headers={'Accept': 'application/json'}, params={'term': search_string})
        
        results = response.json()['results']  # list of dictionaries

        # Display joke to user
        for result in results:
            time.sleep(1)
            print(result['joke'])
            print('')

            another_joke = input(f"Want to hear another {search_string} joke? (y/n): ")

            # while True:
            if another_joke.lower() in ('n','no','nope'):
                break
            elif another_joke.lower() in ('y','yes','yep','ok'):
                continue
            else:
                break

    elif user_action.lower() in ('n','no','nope'):
        break
    else:
        break


