import requests

def random_quote():
    r = requests.get('https://favqs.com/api/qotd')
    data = dict(r.json())
    return data


def filter_quote():
    page = 1
    prompt = input('enter keyword:').lower().strip()
    while True:
        url = f'https://favqs.com/api/quotes?page={ page }&filter={ prompt }'
        r = requests.get(url, headers={
                         'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        data = dict(r.json())
        print(
            f'Showing { len(data["quotes"]) } results with keyword [{ prompt }] on page - { page }')

        for item in data['quotes']:
            print(f"-> '{ item['body'] }' \n- { item['author'] }\n")

        print('------------------------------------------------------------------')

        user_input = input('enter [n]ext,[s]earch, or [q]uit: ')

        if user_input == 'q':
            break
        elif user_input == 'n':
            page += 1
        elif user_input == 's':
            prompt = input('enter keyword:').lower().strip()
        else:
            print('bad input!!!')

    return


def main():
    # # version 1:
    # test_quote = random_quote()
    # print (f"\t{ test_quote['quote']['body'] }\n\t~{ test_quote['quote']['author'] }")
    filter_quote()


if __name__ == '__main__':
    main()
