## Web Scraping for inspirational quotes

##import libraries
from email.quoprimime import quote
from bs4 import BeautifulSoup
import requests
import random
from twilio.rest import Client
import keys
import schedule,time

import smtplib
import ssl
from email.message import EmailMessage


# create list to store scraped data
authors = []
quotes = []

## function to scrape
def get_quotes(page_number):

    page_num = str(page_number)
    url = 'https://www.goodreads.com/quotes/tag/inspirational?page='+page_num
    webpage = requests.get(url) # Make a request
    soup = BeautifulSoup(webpage.text, 'html.parser') #parse the text
    quote_text = soup.find_all('div',attrs={'class': 'quoteText'})

    
    for i in quote_text:
        quote = i.text.strip().split('\n')[0]
        # print(quote)
        #author info
        author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip()
        # print(author)
        quotes.append(quote)
        authors.append(author)

# get_quotes(1)
# print(quotes)
# print(authors)

#loop through n pages and scrape data
n = 10 
for num in range(0,n):
    get_quotes(num)

#combine the list 
combine_list = []
#loop quotes and author list and combine
for i in range(len(quotes)):
    combine_list.append(quotes[i]+'-'+authors[i])

#print(combine_list)


# get a random quote to share

# def send_text(quotes_list=combine_list):
    
#     account = keys.account_sid
#     token = keys.auth_token
#     client = Client(account, token)
#     quote = quotes_list[random.randint(0, len(quotes_list)-1)]

#     client.messages.create(to=keys.my_num,
#                            from_=keys.twilio_num,
#                            body=quote
#                            )
#     print(quote)

# send_text()

### send a message in the morning
# schedule.every().day.at("08:00").do(send_text)

### testing
# schedule.every().day.at("21:30").do(send_text)

# while True:
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(1)


## send an email
def send_email(quotes_list=combine_list):
    subject = "Daily Motivation"
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]
    body = quote
    sender = "jayewhocodes@gmail.com"
    reciever = "jayewhocodes@gmail.com"
    password = input("Enter a password: ")
    message = EmailMessage()
    message["From"] = sender
    message["To"] = reciever
    message["Subject"] = subject
    message.set_content(body)

    html = f"""
    <html>
        <head>
            <title>Daily Motivation</title>
            <link rel="stylesheet" href="style.css">
        <body>
            <h1>{subject}<h/1>
            <p>{body}</p>
        </body>
    </html>
    """
    message.add_alternative(html, subtype="html")
    context = ssl.create_default_context()
    print("Sending")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,reciever,message.as_string())
    print("success")

   


send_email()



 ### testing
    # schedule.every().day.at("08:00").do(send_email,send_text)

    # while True:
    #     # Checks whether a scheduled task
    #     # is pending to run or not
    #     schedule.run_pending()
    #     time.sleep(1)