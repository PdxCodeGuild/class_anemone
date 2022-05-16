import requests

def api_call():
    r = requests.get('https://favqs.com/api/qotd')
    data = dict(r.json())
    return data

def main():
    qotd = api_call()
    
    print (f"\t\t{ qotd['quote']['body'] }\n\t\t~{ qotd['quote']['author'] }")
   

if __name__ == '__main__':
    main()
