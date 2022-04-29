"""lab 4"""
print("""welcome to 'blackjack' advisor-bot: 
random hand generating...
""")
x = 0 # aesthetic addition to simulate loading process for hand dealing
while x < 10000000:
    x += 1

    if x == 2500000:
        print("\n...\n")
    elif x == 5000000:
        print("\n...\n")
    elif x == 7500000:
        print("\n...\n")
    elif x == 9999999:
        print("\n...\n")


# print("hello")
# i created the following list in order to emulate actual probability of 52 card deck random choice without replacement
deck_52_cards = ["A", "A", "A", "A", "K", "K", "K", "K", "Q", "Q", "Q", "Q", "J", "J", "J", "J", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10"]  
# deck_nums = {
#         "2": 2,
#         "3": 3,
#         "4": 4,
#         "5": 5,
#         "6": 6,
#         "7": 7,
#         "8": 8,
#         "9": 9,
#         "10": 10
# }
# deck_face = {
#     "jack": 10,
#     "queen": 10,
#     "king": 10,
#     "ace": 1
# }
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
# below commented out lines were my attempt to create a dict.list,  but commented it out since I ended up making a more simple dictionary
# deck_52 = []
# deck_52.extend(deck_nums)
# deck_52.extend(deck_face)
# print(deck_52.keys())
# print(deck_52.values())
hand = [] # set this as a placement for random selections of cards from deck
import random
# draw = random.choice(deck_52_cards)
# print(draw)

# following is a while look to grab 3 random cards from deck
while len(hand) < 3:
    draw = (random.choice(deck_52_cards))
    hand.append(draw)
    # print(draw)

# below is print of my hand to check to see what you hand is before counting    
print(f"hand: {hand}") # used for code verification, but also for user 
# hand = ['2', '3', '4'] 
# print(options) # used this option to check to see if the cards were pulled correctly conisdering probability without replacement

# function created to go through hand one card at a time and accumulate the total value for advisement
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

count = ct_blk_jk(hand, deck_52) # use of function, assignment of returned value
print(f"count: {count}") # used to code verification check, but also for user 
 

# conditionals for advicement based on random hand dealt: 
if count < 17: 
    print("hit...")
elif 17 <= count <= 20:
    print("stay")
elif count == 21:
    print("BLACKJACK!")   
else:
    print("busted!") 


