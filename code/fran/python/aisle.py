# Capstone (Aisle Finder)
# Fran Kappes

# This program will take in two search parameters (two actors) 
#   and find what common movie they were both in.

import requests
import pprint

# Collect location and product info from user
zip_code = input("Enter your current zip code: ")
product_type = input("What type of product are you looking for (e.g. 'milk' or 'cereal')? ")


# Make first API call to get an access token. Note that this is a POST request.
# "at" refers to access token
# response = requests.get('https://api.kroger.com/v1/', headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Accept': 'application/json'}, params={'filter': quote_filter, 'page': page_num})
# "curl -X POST \\\n  'https://api.kroger.com/v1/connect/oauth2/token' \\\n  -H 'Content-Type: application/x-www-form-urlencoded' \\\n  -H 'Authorization: Basic {{base64(“CLIENT_ID:CLIENT_SECRET”)}}' \\\n  -d 'grant_type=client_credentials&scope={{SCOPE}}'"

# response = requests.get('https://api.kroger.com/v1/connect/oauth2/token', headers={'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic YWlzbGVmaW5kZXItNGU2ZDBiMzI2MDE0YjhiOWNkMTE3OGVmMDk3ZGIwNDkxMzgxNDg4ODk3MTIzOTY5NzUyOmlsblBDZ3ZSSm9FVEktb3FEc21QVmtIZlh5c1VleTl2SHExMF9za0E='},  params={'grant_type': 'client_credentials', 'scope': 'product.compact'})
at_response = requests.post('https://api.kroger.com/v1/connect/oauth2/token', headers={'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic YWlzbGVmaW5kZXItNGU2ZDBiMzI2MDE0YjhiOWNkMTE3OGVmMDk3ZGIwNDkxMzgxNDg4ODk3MTIzOTY5NzUyOmlsblBDZ3ZSSm9FVEktb3FEc21QVmtIZlh5c1VleTl2SHExMF9za0E='},  params={'grant_type': 'client_credentials'})

access_token = at_response.json()['access_token']     

# print(at_response.json())
# pprint.pprint(response.json())
print(access_token)

# Make second API call to fetch a location id, based on zip code
# "loc" refers to location. 
# Response has a default limit of 10 results so will always be on one page (although extendable, that will remain unchanged for this version).
# Mile radius is set to a 10 mile default. That will remain unchanged for this version.
# Note: The access token is only good for 30 minutes. For future versions we'll keep track of time.
#   For this first version, we'll request an access token before calling subsequent set of APIs.

loc_response = requests.get('https://api.kroger.com/v1/locations', headers={'Authorization': 'Bearer '+access_token, 'Cache-Control': 'no-cache'}, params={'filter.zipCode.near': zip_code})

# print(loc_response.json())

loc_results = loc_response.json()['data']     # list of dictionaries

# pprint.pprint(loc_response.json())    # see entire locations response message

for loc_result in loc_results:
    if loc_result['chain'] != 'SHELL COMPANY':
        # print(loc_result['locationId'], ' - ', loc_result['chain'], ' - ', loc_result['name'], ' - ', loc_result['address']['addressLine1']) 
        print(loc_result['name'], ' - ', loc_result['address']['addressLine1'], ' ( Location ID: ',loc_result['locationId'],')') 
    

# Prompt user to enter location id of the store they want
location_id = input("Enter Location ID for the store you want to shop at: ")

# Make third API call to fetch the aisle location for the store and product type of interest
product_response = requests.get('https://api.kroger.com/v1/products', headers={'Authorization': 'Bearer '+access_token, 'Cache-Control': 'no-cache'}, params={'filter.term': product_type, 'filter.locationId': location_id})

print(product_response.request.__dict__)

# The above print statement (with __dict__) produces this output:
# {'method': 'GET', 'url': 'https://api.kroger.com/v1/products?filter.term=milk&filter.locationId=70500205', 'headers': {'User-Agent': 'python-requests/2.27.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXBpLmtyb2dlci5jb20vdjEvLndlbGwta25vd24vandrcy5qc29uIiwia2lkIjoiWjRGZDNtc2tJSDg4aXJ0N0xCNWM2Zz09IiwidHlwIjoiSldUIn0.eyJhdWQiOiJhaXNsZWZpbmRlci00ZTZkMGIzMjYwMTRiOGI5Y2QxMTc4ZWYwOTdkYjA0OTEzODE0ODg4OTcxMjM5Njk3NTIiLCJleHAiOjE2NTMwMDA5NzMsImlhdCI6MTY1Mjk5OTE2OCwiaXNzIjoiYXBpLmtyb2dlci5jb20iLCJzdWIiOiIzZmRkOWVkNi1jNjA3LTVkNWQtOTczMC1lN2EwZTU0NWRhNjIiLCJzY29wZSI6IiIsImF1dGhBdCI6MTY1Mjk5OTE3MzA0MTg2MDI3MSwiYXpwIjoiYWlzbGVmaW5kZXItNGU2ZDBiMzI2MDE0YjhiOWNkMTE3OGVmMDk3ZGIwNDkxMzgxNDg4ODk3MTIzOTY5NzUyIn0.AF3xR1WqHy1g4rNTVhnlVF6rz4Fryf9_BMLYGQqSmcJTtGcdXScYOyFGKY53HXbPa59cQWMgv6BVbH7gPtlAyQ9NU1JO4ZBXXHkjx8Ndy2x4snk9SjQEC0Jk9xucyL7-q6BlcXHKSGawBI1FlKbqNW8Ip2Ei5N8uDJwMGTItCsQHJ1ZGC65-2-C8YqEC1PS9g4LCURqB8KMFxZtdS4M0rDVe_rNQGZ4t92W9eFoJtxAiium_BvL5mfJK_F8eVqu3GzeP9YhNuEmGz8ygsrprK3yVKNWtpSljB5u6l9OpMQrBbWSudJ-hGYNhWvrj0z9Mu1L6cfQMRa0JUq8PuOIUrw', 'Cache-Control': 'no-cache'}, '_cookies': <RequestsCookieJar[]>, 'body': None, 'hooks': {'response': []}, '_body_position': None}



# product_results = product_response.json()['data']     # list of dictionaries
# product_results = product_response.json()    # list of dictionaries

pprint.pprint(product_response.json())    # see entire products response message

# Keep getting this error when I run the program:
# {'code': 'AUTH-1007',
#  'reason': 'Invalid token on request',
#  'timestamp': 1652996090727}

