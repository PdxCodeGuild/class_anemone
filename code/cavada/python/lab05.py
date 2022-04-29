"""lab 5"""
import random

"""get a random set of six digits from 1-99"""
winners = []
while len(winners) < 7:
    draw = random.randint(1,99)
    winners.append(draw)
print(f"\nwinning numbers: {winners}")    

"""create a dictionary to help determine earnings each play"""
lotto = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 2500000
}
"""set a while loop to check 100K and accumulate cash outs per dictionary """
x = 0
bal = 0
winnings = 0
while x < 100000:
    matches = 0
    x += 1
    tix = []
    bal -= 2 
    while len(tix) < 7:
        draw = random.randint(1,99)
        tix.append(draw)
    # print(f"this is ur tick: {tix}")   
    for win in winners:
        if win == tix[0]:
            matches += 1
        tix.pop(0)        
    """convert match # to cash out value"""
    value = lotto[matches]
    # print(f"matches:{matches} cash out: ${value}       ticket purchased: {x} running balance: {bal}")
    bal += value
    winnings += value
"""100k lotto experiment completed and now just need to display my results while also caclulating the ROI"""    
total_cost = x*2
print(f"""\n\t    ending balance: ${bal}\n
            tickets purchased: {x}
            total expenses:    ${total_cost}
            total winnings:    ${winnings} \n
            Return on Investment: {round((bal/total_cost)*100, 2)}%""")
        