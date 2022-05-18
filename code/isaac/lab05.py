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
    earnings = [0, 4, 7, 100, 50000, 1000000, 25000000] # price per winning match
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]: # checking to see if winning and ticket match
            matches += 1
    return earnings[matches]

# assing pick6() to a variable.  Will be used in a for loop
winning = pick6()
expenses = 0

for m in range(100_000): # loop 100,000 times

    ticket = pick6()
    # print(ticket)
    expenses -= 2
    earnings = num_matches(winning, ticket)
    expenses += earnings

def return_on_investment(expenses, earnings):
    roi = (earnings - expenses) / expenses
    return roi 


# print out both expenses and winning tickets
print(winning)
print(expenses, return_on_investment(expenses, earnings))




