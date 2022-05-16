

import random



## pick6 function to create random lottery ticket nums

def pick6():
    nums = []
    for i in range(6):
        lott_nums = random.randint(0,99)
        nums.append(lott_nums)

    return(nums)

# ticket = pick6(nums)
# print(ticket)

# fucntion to determine number of winning tickets 

def num_matches(winning,ticket):
    matches = 0
    for i in range (6):
        if winning[i] == ticket[i]:
            matches += 1
    return(matches)
# winners = num_matches(winning,ticket)
# print(winners)

winnings = {
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:100000,
    6:25000000,
}

balance = 0
expenses = 0
winning_ticket = 0

winning = pick6()

for i in range(100000):
    # print(ticket)
    ticket = pick6()
   
    balance -= 2
    #print(balance)
    expenses += 2

    matches = num_matches(winning,ticket)

    if matches == 1:
        winning_ticket += winnings[matches]

    elif matches == 2:
        winning_ticket += winnings[matches]

    elif matches == 3:
        winning_ticket += winnings[matches]

    elif matches == 4:
        winning_ticket += winnings[matches]

    elif matches == 5:
        winning_ticket += winnings[matches]

    elif matches == 6:
        winning_ticket += winnings[matches]

total_loss = balance + winning_ticket
print(total_loss)


##ROI 
ROI = (winning_ticket - expenses) / expenses
print(ROI)

print(f'Your total loss is {total_loss} and the RoI is {ROI}')



