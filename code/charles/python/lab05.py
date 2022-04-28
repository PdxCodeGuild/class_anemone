import random

opick6 = []
ppick6 = []
balance = 0
t_cost = 2


def pick6(list):
    dpick6 = []
    while len(dpick6) < 6:
        add = random.choice(range(1, 100))
        dpick6.append(add)
    return dpick6

pick6(opick6)
pick6(ppick6)
k = set(opick6)
n = set(ppick6)

def winnings(counter):
    if counter == 0:
        winnings = 0
    elif counter == 1:
        winnings = 4
    elif counter == 2:
        winnings = 7
    elif counter == 3:
        winnings = 100
    elif counter == 4:
        winnings = 50000
    elif counter == 5:
        winnings = 1000000
    elif counter == 6:
        winnings == 25000000
    return winnings

def compare(list1, list2):
    counter = 0
    u = list1 - list2
    if u == 0:
        counter += 1
    elif u != 0:
        counter += 0
    return counter



# def lotto(number):
#     while x < number:
#         return

print(opick6, ppick6)
u = lambda x,y: x - y
i = 0
while i < 5:
    print(u(n,k))
    i = i + 1
    




