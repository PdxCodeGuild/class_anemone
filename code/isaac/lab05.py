'''Pick 6'''
import random

# Generate a list of 6 random numbers representing the winning tickets
def pick6():
    winning_tickets = []
    for i in range(6):
        win_nums = random.randint(1, 99)
        winning_tickets.append(win_nums)
    return winning_tickets

def num_matches(winning, ticket):
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000] # price per winning match
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]: # checking to see if winning and ticket match
            matches += 1
    return payout[matches]

# assing pick6() to a variable.  Will be used in a for loop
winning = pick6()
balance = 0

for m in range(100_000): # loop 100,000 times

    ticket = pick6()
    print(ticket)
    balance -= 2
    payout = num_matches(winning, ticket)
    balance += payout

# print out both balance and winning tickets
print(winning)
print(balance)





