
import requests
import pprint

url = requests.get('https://api.rawg.io/api/platforms?key=48c7cfe6a1ec4e9cbd17cfc91400de82',
    params={'page': 1, 'page_size': 25, 'ordering': '-name'})

platform_data = url.json()

for result in platform_data['results']:
    data_res = f"Platform: {result['name']} -- (ID: {result['id']})"
    print(data_res)
    