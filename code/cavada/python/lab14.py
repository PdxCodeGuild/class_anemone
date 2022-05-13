import requests
import pprint
import time

jokes = []  # list shell created to dump jokes from requests in while loop
x =0
while len(jokes) < 1000 or x < 1000: # set this to get as many dad jokes as possible, but not sure why I only get 15-45 or so jokes each time
    req_head = {'accept':'application/json'} # made headers text a variable
    # req_parm = {'format':'json'} 
    req_url = 'https://icanhazdadjoke.com/' # made url a variable
    resp = requests.get(req_url, headers=req_head) # request with url and headers parameter
    joke = (resp.json()) # read as json data
    if joke in jokes: 
        x +=1
        break
    else:
        jokes.append(joke)# this adds the joke dict to a list for later
        joke = [jokes[jokes.index(joke)]] #this gets the joke # accesses the joke dictionary from the list it's sitting in
        j = joke[0] # this accesses the value of the joke
        print('\n',j['joke']) # prints the joke value separated by line and 
        time.sleep(5)
        print("\tstill not laughing yet???")
        time.sleep(2.5)
        print("\t\twell...how about about another!!!")
        time.sleep(2.5)
    # for jo in joke:
    #     print(joke[jo])
    # print(len(jokes))
# pprint.pprint(jokes)
joke_list = [joke['joke'] for joke in jokes] # saves the joke value entry for key value pair in each joke's dictionary 
    # print(jokes[1])2
jokes_str = '\n'.join(joke_list) # strings the jokes together into a neat, readable text...
# print(jokes_str, len(joke_list))