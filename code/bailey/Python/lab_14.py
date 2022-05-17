'''
Class Anemone
Lab 14
Bailey Baker
'''
import requests

# REPL loop for dad jokes
while True:
    # get joke in JSON format with accept and aaplication/json header
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

    # use .json() method to convert response to a dictionary
    dad_joke = response.json()
    
    # print out dad joke with 'joke' key
    print(f"\n\n{dad_joke['joke']}")
    
    # user input for more dad jokes, 'n' finishes the program
    choice = input("\n\nWould you like to hear another dad joke? y/n: ").lower()

    if choice == 'n':
        break