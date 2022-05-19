import schedule
import os
import time
import random

# have a collection of preset messages we can send
#good morning quotes array

good_morning = [
    "Good morning, I love you",
    "Have a great day!",
    "I don't cook, I don't clean let me tell you how I got this ring  :)"
]

#Step 2 Send preset message using API send_message(my_message[0])
from twilio.rest import Client
# from twilio_credentials import cellphone, twilio_account, twilio_num

cellphone = ''
twilio_num = ''


#take in message and send to phone number
def send_message(quote_list=good_morning):
    account = ''
    token = ''
    client = Client(account,token)
    quote = quote_list[random.randint(0,len(quote_list)-1)]

    # client.messages.create(to=cellphone,from=twilio_num, body = quote)

## pip install schedule library
# quote = good_morning[random.randint(0,len(good_morning))]
schedule.every().day.at("5:30").do(send_message, good_morning[0])

while True:
    schedule.run_pending()
    time.sleep(2)

# Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['AC8b13db7b0422ad7fb620f671bb82d819']
# auth_token = os.environ['005e015240b3fe34717837df3aa16951']
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      
#                  )

# print(message.sid)
