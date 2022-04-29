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
def num_matches():
    return SOMETHING


# Define and initialize balance variable
balance = 0

# Generate the winning ticket. This will be a list of numbers.
winning_ticket = pick6()

# Main loop. This loop will run 100,000 times. Each loop will do a number of things:
#   Generate a lottery ticket and compare the winning numbers to the lottery ticket.
#   Subtract 2 from the balance (you bought a $2 lottery ticket)
#   Find out how many numbers match
#   Add to your balance the winnings from your matches




# Print the final balance
#print(f"Final balance: {balance}")
