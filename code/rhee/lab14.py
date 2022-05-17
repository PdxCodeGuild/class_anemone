
import requests
import json
import time

response = requests.get('https://icanhazdadjoke.com/', headers={"Accept": 'application/json'})

# print(response.url)
# print(response.text)  # 76.105.187.182
# print(response.status_code)  # 200
# print(response.encoding)  # ISO-8859-1
# print(response.headers)  # {'Content-Type': 'text/plain', 'Content-Length': '14', ...}

time.sleep(3)
print('\n')

# print(response.url)

online_joke = json.loads(response.text)

print(online_joke["joke"])
