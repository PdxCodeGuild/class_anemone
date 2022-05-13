import random


def pick6():
    lottery_ticket = []
    for _ in range(6):
        lottery_ticket.append(random.randint(1, 99))
    return lottery_ticket
     




def num_matches(winning, ticket):
    match = 0
    for x in range(len(winning)):
        if winning[x]==ticket[x]:
            match += 1
    return match

winnings = {6:25000000, 5:1000000, 4:50000, 3:100, 2:7, 1:4, 0:0}



winning_ticket = pick6()

balance = 0
earnings = 0
expenses = 0

for _ in range(100000):
    new_ticket = pick6()
    balance -= 2
    expenses += 2
    match = num_matches(winning_ticket, new_ticket)
    earnings += winnings[match]


    

print('balance',(balance + earnings))
print('earning' ,earnings)
print('expenses', expenses)
print('ROI', ((earnings - expenses)/expenses))
