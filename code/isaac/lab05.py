'''Pick 6'''
import random

# Generate a list of 6 random numbers representing the winning tickets

def pick6():
    winning_tickets = []
    for i in range(6):
        win_nums = random.randint(1, 99)
        winning_tickets.append(win_nums)
    print(winning_tickets)


# pick6()

# Start your balance at 0
my_ticket_balance = 0


# Loop 100,000 times, for each loop:
winning_tickets = []
for i in range(6):
    win_nums = random.randint(1, 99)
    winning_tickets.append(win_nums)
print(winning_tickets)
for m in range(100,000):



# Generate a list of 6 random numbers representing the ticket
my_ticket = []
for i in range(6):
    my_nums = random.randint(1, 99)
    my_ticket.append(my_nums)
print(my_ticket)



# Subtract 2 from your balance (you bought a ticket)
total = my_ticket_balance - 2
print(my_ticket, winning_tickets)


# Find how many numbers match
for numbers in winning_tickets:
    if my_ticket[numbers] == winning_tickets[numbers]:
        matches = my_ticket.count() + winning_tickets.count()
        print(matches)



# Add to your balance the winnings from your matches



# After the loop, print the final balance



