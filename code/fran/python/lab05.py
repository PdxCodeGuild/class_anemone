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


##### BEGIN TEST num_matches() #####
#lottery_ticket = pick6()
#winning_ticket = pick6()

# lottery_ticket = [1,2,3,4,5,6]
# winning_ticket = [5,99,2,3,5,76]

# print(f"lottery ticket: {lottery_ticket}")
# print(f"winning_ticket: {winning_ticket}")

# matches = num_matches(lottery_ticket, winning_ticket)
# print(f"matches: {matches}")

##### END TEST num_matches() #####

# Define payout function. This function determines the lottery ticket holder's
#   payout based on the number of matches to the winning ticket
def get_payout(matches):

    # Define payout dictionary
    payout_scale = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }

    payout = payout_scale[matches]

    return payout


# Define and initialize balance variable
balance = 0

# Generate the winning ticket. This will be a list of numbers.
winning_ticket = pick6()
#print(f"winning_ticket: {winning_ticket}")  ### TEST 


# Main loop. This loop will run 100,000 times. Each loop will do a number of things:
#   Generate a lottery ticket and compare the winning numbers to the lottery ticket.
#   Subtract 2 from the balance (you bought a $2 lottery ticket)
#   Find out how many numbers match
#   Add to your balance the winnings from your matches

total_winning_payout =  0   # test variable
total_num_wins = 0   # test variable

i = 0

while i < 100000:

    # pay $2 for a ticket
    balance -= 2  
    #print(f"balance at beginning of this loop: {balance}")  ### TEST
    
    # get lottery ticket
    lottery_ticket = pick6()  
    #print(f"lottery ticket: {lottery_ticket}")  ### TEST

    # find out if any numbers match
    matches = num_matches(lottery_ticket, winning_ticket)
    #print(f"matches: {matches}")   ### TEST

    # find out winning payout, if any, for this ticket
    payout_amount = get_payout(matches)
    #print(f"payout_amount: {payout_amount}")   ### TEST

    if payout_amount > 0:
        total_winning_payout += payout_amount
        #total_num_wins += 1   ### TEST
        
        # print(f"payout_amount: {payout_amount}")  ### TEST

    # add winnings payout to balance
    balance += payout_amount
    #print(f"balance at end of this loop: {balance}")  ### TEST

    # increment loop counter
    i += 1

# Calculate ROI (return on investment)
# Note: total expenses = 100,000 tickets * $2 per ticket = 200,000
#   Because number of tickets is hard-coded, I'm hard-coding the total expenses
roi = (total_winning_payout - 200000)/200000

# format final balance and total winning payout
balance = "${:,}".format(balance)
total_winning_payout = "${:,}".format(total_winning_payout)


# Print the final balance
print(' ')
print(f"Final balance: {balance}")
print(f"Total earnings: {total_winning_payout}")
print("Total expenses: $200,000")
print(f"ROI: {roi}")
#print(f"total number of wins: {total_num_wins}")   ### TEST
print(' ')
