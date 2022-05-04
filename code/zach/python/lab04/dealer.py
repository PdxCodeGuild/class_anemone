import random
from variables import *

def build_deck():
    deck = []
    deck_shuffled = {} 
    for suit in suits:
        for card in cards:
            deck.append(card+' '+suit )
    random.shuffle(deck)

    for card in deck:
        deck_shuffled[card] = cards_val[card[0]]
    return deck_shuffled
    #return print(deck, len(deck))


