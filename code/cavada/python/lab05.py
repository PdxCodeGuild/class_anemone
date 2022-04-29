"""lab 5"""
import random

# used this as example set of tickets to quality check my subsequent function
# winner = ['82', '78', '55', '50', '60', '70']
# ticket = ['82', '78', '55', '65', '27', '58']

# used this to check my function that gives me the winnings per "ticket purchase"
def earnings(matches):
    lotto_dict = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
    }
    key = lotto_dict[matches]
    # print(f"im in the function and this the key: {key}, and this is the type: {type(key)}")
    return key
    
bal = 0 # set for running balance
x = 0 # set this to trip the subsequent while loop at it's 100kth loop

while x < 100000: # set up to simulate 100k lotto ticket purchases
    pick6_win = [] # dump for rando winning ticket nums
    ticket = [] # dump for rando ticket nums
    bal -= 2 # run this operation to simulate a single purchase of $2 ticket during each while loop(100k total so total cost will be 200k)
    while len(pick6_win) < 6: # while loop used to gather six random numbers from 1 - 99 to represent winning ticket numbers 
        pick = str(random.randint(1, 99)) 
        # print(pick)
        pick6_win.append(pick)
    # print(pick6_win)
    while len(ticket) < 6: # while loop used to gather six random numbers from 1 - 99 to represent purchased ticket numbers
        pick = str(random.randint(1,99))
        # print(pick)
        ticket.append(pick)
    # print(ticket)
    matches = 0
    for win in pick6_win: # for loop to determine the earnings by counting 'matches' between winning number and purchased ticket
        if win in ticket:
            matches += 1
    # print(matches)
    
    bal += earnings(matches) # operation included to add each 'play' earnings to balance
    # print(f"""
    # balance is at: {bal}""")
    x += 1
    # print(x)
total_cost = x * 2  # use this to calc total cost of playing lotto 100k times

def ROI(bal, total_cost): # made function to 
    return round((bal/total_cost)*100)

invest_return = ROI(bal, total_cost)

print(f"tickets purchased:   {x} tickets")
print(f"total cost:          ${total_cost}")    
# print(f"ending balance:      ${bal}")
print(f"profit:              ${bal}")
print(f"\nReturn on Investment: {invest_return}%")




