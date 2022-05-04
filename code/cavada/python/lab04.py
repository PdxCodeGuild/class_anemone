# lab 4
print("""welcome to 'blackjack' advisor-bot: 
""")
def ct_blk_jk(hand, deck_52):
    value = hand[0]
    first = int(deck_52[value])
    hand.pop(0)
    value = hand[0]
    second = int(deck_52[value])
    hand.pop(0)
    value = hand[0]
    third = int(deck_52[value])
    count = int(first) + int(second) + int(third)
    return count
x = 1999999
def advice(count):
    if count < 17: 
        message = "hit..."
    elif 17 <= count <= 20:
        message = "stay"
    elif count == 21:
        message ="BLACKJACK!"   
    else:
        message = "busted!"
    return message     
# def loading(x):
#     x = 0
#     while x < 1000000:
#         x += 1
#         if x == 333333:
#             print("...")
#         elif x == 666666:
#             print("...")
#         elif x == 999999:
#             print("...")
#     value = deck_52[draw]
#     print('near end of while loading while loop:',value)
#     print(f"card: {draw} value: {value} advice: {advice(value)}")
# i created the following list in order to emulate actual probability of 52 card deck random choice without replacement
deck_52_cards = ["A", "A", "A", "A", "K", "K", "K", "K", "Q", "Q", "Q", "Q", "J", "J", "J", "J", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10"]  
# following is a dictionary of the values for each possible card, and as you can see from above, I initially tried to create a more complicated dictionary with nested dictionaries, but honestly don't understand dictionaries enough to know if it's worth it
deck_52 = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 1
}
hand = [] # set this as a placement for random selections of cards from deck
import random
num = 1
run_tot=0
while len(hand) < 3:
    input(f"hit any key to draw card({num}): ")
    num +=1
    draw = (random.choice(deck_52_cards))
    print("\tcard:", draw)
    ad = advice(deck_52[draw])
    hand.append(draw)
    run_tot += deck_52[draw]
    print(f"\tcurrent hand: {hand} \n\trunning total: {run_tot}")
    print(f"\tadvice: {advice(run_tot)}\n")
# below is print of my hand to check to see what you hand is before counting    
print(f"hand: {hand}") # used for code verification, but also for user 
# hand = ['2', '3', '4'] 
# print(options) # used this option to check to see if the cards were pulled correctly conisdering probability without replacement
# function created to go through hand one card at a time and accumulate the total value for advisement
count = ct_blk_jk(hand, deck_52) # use of function, assignment of returned value
print(f"full hand: {count}") # used to code verification check, but also for user 
 
print(advice(count)) # final advice for full hand (3 cards)
