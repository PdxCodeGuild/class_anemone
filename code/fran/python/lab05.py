# Lab05 - Pick 6
# Fran Kappes

import random

# Define pick6 function, that randomly generates 6 numbers
# This will be used to generate the winning numbers and the 100,000 lottery tickets
def pick6():

    # Define list that will store numbers entered by user
    nums = []

    i = 0

    while i < 6:
        nums.append(random.randint(1,99))
        i += 1
    return nums

# Define num_matches function, which determines the number of matches
#   between the winning numbers and a lottery ticket
def num_matches(lottery_ticket, winning_ticket):
    # Define and initialize matches counter
    matches = 0

    # Compare the lottery ticket numbers to the winning ticket numbers
    # To be a match, numbers in the same position for both tickets must match 
    i = 0
    
    while i < 6:
        if int(lottery_ticket[i]) == int(winning_ticket[i]):
            matches += 1

        i += 1

    return matches

# TEST num_matches()
#lottery_ticket = pick6()
#winning_ticket = pick6()

lottery_ticket = [1,2,3,4,5,6]
winning_ticket = [5,99,2,3,5,76]

print(f"lottery ticket: {lottery_ticket}")
print(f"winning_ticket: {winning_ticket}")

matches = num_matches(lottery_ticket, winning_ticket)
print(f"matches: {matches}")

# END TEST num_matches()

# Define and initialize balance variable
#balance = 0

# Generate the winning ticket. This will be a list of numbers.
#winning_ticket = pick6()

# Main loop. This loop will run 100,000 times. Each loop will do a number of things:
#   Generate a lottery ticket and compare the winning numbers to the lottery ticket.
#   Subtract 2 from the balance (you bought a $2 lottery ticket)
#   Find out how many numbers match
#   Add to your balance the winnings from your matches

i = 0

while i < 100000:

    lottery_ticket = pick6()

    matches = num_matches(lottery_ticket, winning_ticket)





# Print the final balance
#print(f"Final balance: {balance}")
