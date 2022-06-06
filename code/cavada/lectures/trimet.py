# response = requests.get("https://developer.trimet.org/ws/v2/vehicles", params={'appID': 'D065A3A5DAE4622752786CEB9', 'routes': 70"})
import time
import json
import pprint


    page = 1
    search = input("\nsearch for quotes by keyword?? ")
    keyword = input('keyword: ')
    while search != 'n':
        page_filt = f"page={x}&"
        url = f'https://favqs.com/api/quotes/?{page_filt}filter={keyword}'
        print(f"\tpage: {page}")
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get(url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        resp = response.json()
        quotes = resp['quotes'] 
        print(f"{len(quotes)} quotes associated with {keyword}\n")
        print("Pick from list of authors: 'enter corresponding digit' ")
        page +=1
        authors = {}
        for i , quote in enumerate(quotes):
            auth = {}
            # print(quote['author'])
            auth = {i:quote['author']}
            author_a = quote['author']
            authors.update(auth)
        # print(authors)
        # authors = set(authors)
        # print(authors)
        auth_list = []
        for i, auth in enumerate(authors):
            print(f"{i} - {authors[auth]} -")
            # print(f"\t({i}) {authors[i]}")
            auth
        # pprint.pprint(quotes)    
        choice = int(input(': '))
        a = authors[choice]
        x+=1  
        for quote in quotes:
            if quote['author']== a:
                # pprint.pprint('\n\t',quote['body'],'\n\n\t-',a,'\n')
                print(f"\n\t{quote['body']}\n\n\t -{a}\n")
                time.sleep(1)
            elif quote['body'] == 'No quotes found':
                break
            # time.sleep(1)
        if resp['last_page']==True:
            # (resp['last_page'])
            print('No other pages to search...')
            break
        else:
            print('there are more pages to search...')
            search = input(f"\tenter to next page ({page})? ")
