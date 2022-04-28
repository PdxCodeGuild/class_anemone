import random
from variables import *

def deck_builder():
    deck = []
    deck_shuffled = {} 
    for suit in suits:
        for card in cards:
            deck.append(card+' '+suit )
    random.shuffle(deck)

    for card in deck:
        deck_shuffled[card] = cards_val[card[0]]
    return deck


