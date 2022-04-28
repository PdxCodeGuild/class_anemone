# ....Lab 05 Version 1

import random

# generate a list of 6 random numbers (COMPLETE)
def pick6():
    x = []
    for i in range(6):
        r = random.randint(1, 99)
        x.append(r)
    return x

# money = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}

# define a function to match winning ticket to user ticket (?)
def num_matches(winning, ticket):
    money = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1
        earnings = money[matches]
    return earnings

def lottery():
    wallet = 0
    winning = pick6()
    for i in range(100000):
        ticket = pick6()
        wallet - 2
        num_matches(winning, ticket) + wallet
    final_balance = wallet
    print(final_balance)


print(lottery())