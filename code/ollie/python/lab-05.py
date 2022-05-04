import random

def pick6():
    ticket = []
    for i in range(6):
        nums = random.randint(1, 99)
        ticket.append(nums)
    return ticket

match_dict = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}

balance = 0

def num_matches(winning, user):
    matches = 0
    for i in range(len(user)):
        if winning[i] == user[i]:
            matches += 1
        money = match_dict[matches]
    return money

def winnings():
    win = 0
    loss = 0
    winning_ticket = pick6()
    for i in range(100000):
        user_ticket = pick6()
        loss = loss - 2
        win += num_matches(winning_ticket, user_ticket)
    earnings = win + loss
    return earnings

print(f"""
Final Balance ($): {winnings()}
ROI: {(winnings() - 200000) / 200000}
""")