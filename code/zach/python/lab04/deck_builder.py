from variables import *

def deck_builder(suits_lis, cards_dic):
    deck = {}
    for suit in suits_lis:
        for card in cards_dic:
            deck[suit+card] = cards_dic[card] 

    print(deck)

deck_builder(suit_val, card_val)