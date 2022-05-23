import requests
import json


def get_quote():
    while True:
        page = 0
        search = input("enter a keyword to search for quotes or 'e' to exit: ").lower()
        if search == "e":
            break

        while True:
            response = requests.get("https://favqs.com/api/quotes?page=<page>&filter=<keyword>",
                                    params={"filter": search, "page": page},
                                    headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            
            data_type = json.loads(response.text)
            page = data_type["page"]
            quote_data = data_type["quotes"]

            for quote in quote_data:
                author = quote["author"]
                quote = quote["body"]
                print(f"{quote} - {author} "
                      f"\n")

            user_input = input(f"You are on page {page} enter 'n' for next page or 'e' to exit: ").lower()
            if user_input == 'n':
                page = page + 1
                continue
            elif user_input == 'e':
                print("Goodbye! ")
                break


get_quote()
