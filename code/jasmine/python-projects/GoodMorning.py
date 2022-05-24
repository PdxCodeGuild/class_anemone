import schedule
import time
import random

# have a collection of preset messages we can send
#good morning quotes array

good_morning = [
    "Good morning, I love you",
    "Have a great day!",
    "Take care of yourself today!"
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
# quote = good_morning[random.randint(0,len(good_morning))]


## pip install schedule library

schedule.every().day.at("5:30").do(send_message, good_morning[0])

while True:
    schedule.run_pending()
    time.sleep(1)


