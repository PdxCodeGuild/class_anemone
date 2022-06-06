import requests
# create quote function to retrieve quotes from favqs API based on page and search term
def quote(search_term, page=1):
    response = requests.get("https://favqs.com/api/quotes/", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'page' : page, 'filter': f'{search_term}'})
    quote_dict = response.json()
    return quote_dict

quote_string = ''
page = 1

# create loops to get the search term and display the quotes with the authors. Create exception if no search results are found.
while True:
    search_term = input(f"\nEnter a keyword to look for related quotes or type 'done' to exit: ")
    if search_term in ['d', 'done', 'exit', 'quit']:
        break

    while True:
        try:
            for quotes in quote(f'{search_term}', page)['quotes']:
                quote_string += f"\n\"{quotes['body']}\"\nAuthor: {quotes['author']}\n\n"
            print(quote_string)
            next_page = input(f"That's it for page {page}! Would you like to go to the next page (yes/no)? ")
            if next_page in ['no', 'n']:
                break
            else:
                page += 1
        except KeyError:
            print(f"\nNo more results found for {search_term} please try another search term.\n")
            break