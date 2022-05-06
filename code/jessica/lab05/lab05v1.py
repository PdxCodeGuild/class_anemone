import random

## Steps-------->>>>

"""

1. Generate a list of 6 random numbers representing the winning tickets
2. Start your (earnings) balance at 0
2. Loop 100,000 times, for each loop:
3. Generate a list of 6 random numbers representing the ticket
4. Subtract 2 from your balance (you bought a ticket)
5. Find how many numbers match 
6. Add to your balance the winnings from your matches
7. After the loop, print the final balance 

"""
winning_numbers = []

def pick6():
    draw_numbers = []
    for i in range(6):
        draw_numbers.append(random.randint(1,99))
    return draw_numbers

def num_matches(winning_numbers, draw_numbers):
    matches = 0 #starting matches at zero
    for win, tix in zip(winning_numbers, draw_numbers):
        if win == tix:
            matches += 1
    return matches

winning_numbers = pick6()

winnings = {6: 25000000, 5: 1000000, 4: 50000, 3: 100, 2: 7, 1: 4, 0: 0}

balance = 0
earnings = 0
expenses = 0

for _ in range(10000000000000):
    current_ticket = pick6()
    balance -= 2
    expenses += 2
    matches = num_matches(winning_numbers, current_ticket)
    balance += winnings[matches]
    earnings += winnings[matches]

print('balance', balance)
print('earnings', earnings)
print('expenses', expenses)
print('ROI', (earnings - expenses) / expenses)
    