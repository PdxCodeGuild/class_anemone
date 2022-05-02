'''
class_anemone
Lab 5
Bailey Baker
'''
import random

winning = []
ticket = []
balance = 0
i = 100000
earnings = 0
expenses = 0

def pick6(num):
    num = []
    for i in range(6):
        num.append(random.randint(1,99))
    return num

def num_matches(winning, ticket):
    counter = 0
    for x in range(6):
        if winning[x] == ticket[x]:
            counter += 1
    return counter

while i > 0:
    i -= 1
    balance -= 2
    expenses += 2
    winning = pick6(winning)
    ticket = pick6(ticket)
    matches = num_matches(winning, ticket)
    if matches == 1:
        balance += 4
        earnings += 4
    elif matches == 2:
        balance += 7
        earnings += 7
    elif matches == 3:
        balance += 100
        earnings += 100
    elif matches == 4:
        balance += 50000
        earnings += 50000
    elif matches == 5:
        balance += 1000000
        earnings += 1000000
    elif matches == 6:
        balance += 25000000
        earnings += 25000000

investment = ((earnings - expenses) / expenses)*100
print (f'''After 100,000 tickets your total balance is: {balance}
Your total winnings with the tickets were: {earnings}
Your ROI(Return on Investment) was: {investment}%''')