import requests, time # import requests and time

# create dad_joke function to retrieve dad joke dict from API
def dad_joke(search_term, page=1):
    response = requests.get("https://icanhazdadjoke.com/search", headers={'accept': 'application/json'}, params={'page' : page, 'limit' : 5, 'term': f'{search_term}'})
    joke_dict = (response.json())
    return joke_dict

# create for loop that rests index to 0 and page to 1. Also defines search_term variable as empty string to put user response into
while True:
    index = 0
    page = 1 
    search_term = ''
    user_response = input("\nWhat type of dad joke would you like to search for or type 'done' to quit: ")
    if user_response in ['done', 'd', 'exit']:
        break

    # create loop if user enters search term
    else:
        while True:
            try:
                time.sleep(4) ### to make testing faster you can comment this line out
                # prints the joke at the given index with a delay if there is no error (index out of range due to running out of jokes) 
                print('\n' + dad_joke(user_response, page)['results'][index]['joke'])
                if index < 4:
                    index += 1
                elif index == 4:
                    next_page = input("\nYou have run out of jokes on this page. Would you like to go to the next page? (y/n): ")
                    if next_page.lower() in ['yes', 'y']:
                        page += 1
                        index = 0
                    else:
                        print(f"\nI hope you enjoyed the '{user_response}' dad jokes!")
                        break
            # if there is an indexerror than the loop will break and user can try a new search
            except IndexError:
                print(f"\nYou've run out of '{user_response}' jokes! Please try another search.")
                break