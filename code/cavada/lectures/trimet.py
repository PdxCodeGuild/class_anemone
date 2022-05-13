import json
import pprint
import requests
response = requests.get('https://developer.trimet.org/ws/v2/vehicles?appID=D065A3A5DAE4622752786CEB9')
# response = requests.get("https://developer.trimet.org/ws/v2/vehicles", params={'appID': 'D065A3A5DAE4622752786CEB9', 'routes': 70"})


pprint.pprint(response.json())

# for resp in response:
#     for r in resp:
#         if resp == 'vehicle'
#         (resp[r])