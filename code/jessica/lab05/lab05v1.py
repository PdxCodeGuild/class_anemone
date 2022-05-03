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
        n = random.randint(1,99)
        draw_numbers.append(n)
    return draw_numbers

def num_matches(winning_numbers, draw_numbers):
    money_value = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
    matches = 0
    for i in range(6):
        if draw_numbers[i] == winning_numbers[i]:
            matches += 1
        earnings = money_value[matches]
    return earnings

def winning_value():
    winner = 0
    loser = 0
    winning_ticket = pick6()
    for i in range(100000):
        personal_ticket = pick6()
        loser = loser - 2
        winner += num_matches(winning_ticket, personal_ticket)
    earnings = winner + loser
    return earnings


print(f"Earnings = {winning_value()}")

#___________version 2_____________#

roi = (winning_value() - 200000) / 200000

print(f"Earnings = {winning_value()} ROI = {roi}")