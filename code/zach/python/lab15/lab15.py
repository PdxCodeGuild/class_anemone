import random
import requests

def random_quote():
    r = requests.get('https://favqs.com/api/qotd')
    data = dict(r.json())
    return data

def main():
    random_quote = random_quote()
    
    print (f"\t\t{ random_quote['quote']['body'] }\n\t\t~{ random_quote['quote']['author'] }")
   

if __name__ == '__main__':
    main()
