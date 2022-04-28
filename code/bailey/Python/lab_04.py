'''
class_anemone
Lab 4
Bailey Baker
'''
# Dictionary to store all cards values
playing_cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
     'J': 10,
     'Q': 10,
     'K': 10
}

#Gather users 3 cards
card1 = str(input("what's your first card?: ")).upper()
card2 = str(input("what's your second card?: ")).upper()
card3 = str(input("what's your third card?: ")).upper()

#function to return sum of three cards
def card_sum(card1, card2, card3):
    return card1 + card2 + card3

#If statements to show proper advice depending on sum of three cards
if card_sum(playing_cards[card1], playing_cards[card2], playing_cards[card3]) == 21:
    print(f"{card_sum(playing_cards[card1], playing_cards[card2], playing_cards[card3])} Blackjack!")
elif card_sum(playing_cards[card1], playing_cards[card2], playing_cards[card3]) > 21:
    print(f"{card_sum(playing_cards[card1], playing_cards[card2], playing_cards[card3])} Already Busted")
elif card_sum(playing_cards[card1], playing_cards[card2], playing_cards[card3]) >= 17:
    print(f"{card_sum(playing_cards[card1], playing_cards[card2], playing_cards[card3])} Stay")
elif card_sum(playing_cards[card1], playing_cards[card2], playing_cards[card3]) < 17:
    print(f"{card_sum(playing_cards[card1], playing_cards[card2], playing_cards[card3])} Hit")

