import random

import dealer
import variables


def bj_game():
    game_deck = dealer.build_deck()
    deal_count = 0
    hand_count = 0
    p_hand = []
    d_hand = []
    game_deck = []

    bj_shuffle(game_deck, d_hand, p_hand)
    for i in range (0,55):
        deal(p_hand, game_deck)
    print( len(game_deck), p_hand, d_hand)



def bj_shuffle(deck, dealer, player):
    # create deck using lists found in variables.py
    for suit in variables.suits:
        for card in variables.cards:
            deck.append(f'{ card } { suit }')


    for i in range(2):
        # draw random cards from deck
        p_card = random.choice(deck)
        d_card = random.choice(deck)
        # remove cards from deck
        deck.remove(p_card)
        deck.remove(d_card)
        # add cards to players' hands
        dealer.append(d_card)
        player.append(p_card)

    return deck, dealer, player

def deal(target_hand, deck):
    try:
        card = random.choice(deck)
        deck.remove(card)
        target_hand.append(card)
    except:
        print('deck out of cards')

    return target_hand, deck

bj_game()
