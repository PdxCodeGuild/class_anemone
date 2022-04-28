#Lab 5

#Step 1: Generate a list of 6 random numbers

import random

ticket_nums = []
random_nums = random.randint(0,99)
#______________________________________________
def pick6():                                           
    for i in range (6):
        random_nums = random.randint(0,99)          
        ticket_nums.append(random_nums)                                 
            
    return (ticket_nums)
#______________________________________________


#Step 2: Start balance at 0
starting_balance = 0



