"""lab 16"""

import requests

"""create logitech acct"""

url = "https://accounts.logi.com/identity/oauth2/createandsignin"
payload = {
    "email": "cavada.jonathon@gmail.com",
    "email_verified": True,
    "password": "^213Logi908^",
    "channel_id": "",
    "locale": "en-US"
}
headers = {
    "Accept": "application/json",
    "X-Forwarded-For": "76.115.162.123",
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
print(response.text)

"""create circle acct"""

url = "https://api.circle.logi.com/api/accounts"
payload = {"marketingOptIn": 0}
headers = {
    "Accept": "application/json",
    "X-API-Key": "abc123",
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
print(response.text)

"""get acct"""

url = "https://api.circle.logi.com/api/accounts/self"
headers = {
    "Accept": "application/json",
    "X-API-Key": "abc123"
}


response = requests.get(url, headers=headers)


print(response.text)








"""Get Live WebRTC Offer"""

# url = "https://api.circle.logi.com/api/accessories/accessory_id/live/webrtc/offer?audio=sendrecv&video=sendonly"
# headers = {
#     "Accept": "application/json",
#     "X-API-Key": "abcd123"
# }
# response = requests.get(url, headers=headers)
# print(response.text)

# """Provide Live WebRTC Answer Async"""

# url = "https://api.circle.logi.com/api/accessories/accessory_id/live/webrtc/session_id/answer"
# headers = {
#     "Accept": "text/plain",
#     "X-API-Key": "abcd123",
#     "Content-Type": "application/json"
# }
# response = requests.post(url, headers=headers)
# print(response.text)

# """Provide Live WebRTC Offer and Get Answer"""

# url = "https://api.circle.logi.com/api/accessories/accessory_id/live/webrtc/offer_answer"
# headers = {
#     "Accept": "application/json",
#     "X-API-Key": "abcd123",
#     "Content-Type": "application/json"
# }
# response = requests.post(url, headers=headers)
# print(response.text)

# """Renegotiate Live WebRTC"""

# url = "https://api.circle.logi.com/api/accessories/accessory_id/live/webrtc/session_id/offer"
# headers = {
#     "Accept": "application/json",
#     "X-API-Key": "abcd123",
#     "Content-Type": "application/json"
# }
# response = requests.post(url, headers=headers)
# print(response.text)

# """Stop Live WebRTC"""

# url = "https://api.circle.logi.com/api/accessories/accessory_id/live/webrtc/session_id"
# headers = {
#     "Accept": "application/json",
#     "X-API-Key": "abcd123"
# }
# response = requests.delete(url, headers=headers)
# print(response.text)