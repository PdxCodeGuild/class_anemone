


import random

nums = []

## pick6 function to create random lottery ticket nums

def pick6(nums):
    for i in range(6):
        lott_nums = random.randint(0,99)
        nums.append(lott_nums)

    return(nums)

ticket = pick6(nums)
print(ticket)



winning = {
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:100000,
    6:25000000,

}
# fucntion to determine number of winning tickets 

def num_matches(winning,ticket):
    matches = 0
    for i in range(6):
        if winning[i] == ticket[i]:
            matches += 1
    return(matches)

winners = num_matches(winning,ticket)
print(winners)

balance = 0

winning_ticket = 0

for i in range(100000):
    balance = balance - 2
    #print(balance)

    if winners == 1:
        winning_ticket += ticket[winners]

    elif winners == 2:
        winning_ticket += ticket[winners]

    elif winners == 3:
        winning_ticket += ticket[winners]

    elif winners == 4:
        winning_ticket += ticket[winners]

    elif winners == 5:
        winning_ticket += ticket[winners]

    elif winners == 6:
        winning_ticket += ticket[winners]

total_loss = balance + winning_ticket

print(f'Your have won {winners} and you have {total_loss} $ left to spend')