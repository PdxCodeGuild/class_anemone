import re
import requests

req_head = {'accept':'application/json'}
req_parm = {'format':'json'}
req_url = 'https://icanhazdadjoke.com/'
resp = requests.get(req_url, header=req_head)