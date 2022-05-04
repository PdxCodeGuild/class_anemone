import random


def pick6():
    lottery_ticket = []
    for x in range(6):
        lottery_ticket.append(random.randint(1, 99))
    return lottery_ticket
     
win = pick6()
balance = 0

for x in range(100000):
    lottery_ticket = pick6()
    balance =  - 2
    payment = [0,4,7,100,50000,1000000,25000000]
    lottery_ticket = pick6()
print(balance)