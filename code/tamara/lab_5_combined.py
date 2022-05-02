
# use random function for random numbers
import random

# define function for randomly generating ticket
def ticket():
    # empty list to hold 6 random numbers generated between 1-99 and added to end of list
    ticket_numbers = []
    for number in range(6):
        ticket_numbers.append(random.randint(1, 99)) # make sure to change the random int 1-3 to what its supposed to be
    # returns the ticket_numbers list 
    return ticket_numbers 

# set balance, winnings, expenses to 0 and generate a random winning_ticket 
balance = 0
winnings = 0
expenses = 0
winning_ticket = ticket()
print(f'The winning ticket is {winning_ticket}')

# set total number of tickets and x for countdown of while loop
total_tickets = 100000
x = 0

# create while loop so it will loop 100000 times, create bought_ticket for each loop and set number of matches to 0 at start of each loop
while x < total_tickets:
    bought_ticket = ticket()
    number_matches = 0

    # determine number of matches between bought ticket and winning ticket
    if bought_ticket[0] == winning_ticket[0]:
        number_matches = number_matches + 1
    if bought_ticket[1] == winning_ticket[1]:
        number_matches = number_matches + 1
    if bought_ticket[2] == winning_ticket[2]:
        number_matches = number_matches + 1
    if bought_ticket[3] == winning_ticket[3]:
        number_matches = number_matches + 1
    if bought_ticket[4] == winning_ticket[4]:
        number_matches = number_matches + 1
    if bought_ticket[5] == winning_ticket[5]:
        number_matches = number_matches + 1
    
    # determine the winnings and balance for the round and add it to these variables which are outside the loop so they will hold a running sum
    if number_matches == 1:
        winnings = winnings + 4
        balance = balance + 4
    if number_matches == 2:
        winnings = winnings + 7
        balance = balance + 7
    if number_matches == 3:
        winnings = winnings + 100
        balance = balance + 100
    if number_matches == 4:
        winnings = winnings + 50000
        balance = balance + 50000
    if number_matches == 5:
        winnings = winnings + 1000000
        balance = balance + 1000000
    if number_matches == 6:
        winnings = winnings + 25000000
        balance = balance + 25000000
    
    # subtract the cost of the ticket from the balance and add the cost to expenses
    balance = balance - 2
    expenses = expenses + 2
    # count the loop for countdown
    total_tickets = total_tickets - 1

ROI = balance/200000

print(f'Your balance is {balance}$, your ROI is {ROI}, your winnings are {winnings}$ and your expenses were {expenses}$')