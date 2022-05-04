#Lab 5

import encodings
import random
#______________________________________________
def pick6():                                           
    ticket_nums = []
    for i in range (6):
        random_nums = random.randint(0,99)          
        ticket_nums.append(random_nums)                                 
            
    return (ticket_nums)
#______________________________________________
#______________________________________________
def num_matches(winning, ticket):
    matches = 0
    for i in range (6):
        if winning[i] == ticket[i]:
            matches += 1

    return (matches)
#______________________________________________    

winnings = {

    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000,

}

balance = 0
expenses = 0

total_winnings = 0

winning = pick6()

for i in range (100000):
    ticket = pick6()
    #print("ticket",ticket)

    balance -= 2
    expenses += 2

    matches = num_matches(winning, ticket)

    if matches == 1:
        total_winnings += winnings[matches]
    elif matches == 2:
        total_winnings += winnings[matches]
    elif matches == 3:
        total_winnings += winnings[matches]
    elif matches == 4:
        total_winnings += winnings[matches]
    elif matches == 5:
        total_winnings += winnings[matches]
    elif matches == 6:
        total_winnings += winnings[matches]
    

ending_balance = balance + total_winnings
    
print (f"\nWinning Ticket Numbers: {winning} \nYour balance is: {balance} \nYour total winnnings are: {total_winnings} \nYour ending balance is: {ending_balance}")


#Version 2
#ROI = (earnings - expenses)/expenses

ROI = (total_winnings - expenses) / expenses

print (f"\nROI: {ROI} \nEarnings: {total_winnings} \nExpenses: {balance}\n")




