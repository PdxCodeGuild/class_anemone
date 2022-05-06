import random

def pick6():
    ticket = []
    for i in range(6):
        nums = random.randint(1, 99)
        ticket.append(nums)
    return ticket
    #OR EVERYTHING IN ONE LINE ==> return [random.randint(1, 99) for _ in range(6)]

match_dict = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}

def winnings(winning, user):
    matches = 0
    for i in range(len(user)):
        if winning[i] == user[i]:
            matches += 1
        money = match_dict[matches]
    return money

balance = 0
expenses = 0
earnings = 0
winning_ticket = pick6()
for i in range(100000):
    user_ticket = pick6()
    balance -= 2
    expenses += 2
    earnings += winnings(winning_ticket, user_ticket)
balance += earnings

print(f"""
Final Balance ($): {balance}
ROI: {(earnings - expenses) / expenses}
""")