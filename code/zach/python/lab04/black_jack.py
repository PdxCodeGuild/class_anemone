import random

import dealer
import variables


def bj_game():
    p_hand = []
    d_hand = []
    game_deck = []

    game_deck, d_hand, p_hand = bj_shuffle()
    dealer_tot, player_tot = bj_score(d_hand, p_hand)

    print (len(game_deck), d_hand, p_hand, dealer_tot, player_tot)
    # play = 'y'
    # while play == 'y':


    # * Testing:
    # for i in range (0,55):
    #     deal(p_hand, game_deck)
    # print( len(game_deck), p_hand, d_hand)



def bj_shuffle():
    # create deck using lists found in variables.py
    deck = []
    for suit in variables.suits:
        for card in variables.cards:
            deck.append(f'{ card } { suit }')

    player = []
    dealer = []
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

def bj_deal(target_hand, deck):
    try:
        card = random.choice(deck)
        deck.remove(card)
        target_hand.append(card)
    except:
        print('deck out of cards')

    return target_hand, deck

def bj_score(dealer, player):
    p_score = 0
    d_score = 0
    # score calculated by using first char in index item as key for variables.card_val 
    for card in player:
        p_score += variables.card_val[card[0]]
    for card in dealer:
        d_score += variables.card_val[card[0]]   
    
    return d_score, p_score

def bj_hint():
    pass




bj_game()
