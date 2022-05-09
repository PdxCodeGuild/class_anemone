import random

import dealer
import variables


def bj_game():
    # p_hand = []
    # d_hand = []
    game_deck = []
    
    game_deck, d_hand, p_hand = bj_shuffle(game_deck)
    
    # User Input
    print('♠️ ♥️ ♣️ ♦️ BlackJack ♠️ ♥️ ♣️ ♦️')
    print(f'\nDEALER: | * |{d_hand[1]}\nPLAYER: ', *p_hand, sep = "")
    print('\n♠️ ♣️ ♦️ ♠️ ♥️ ♦️ ♠️ ♥️ ♣️ ♠️ ♥️ ♣️ ♦️')
    user_ip = input('\nEnter [hit,stay,help,exit]: ').lower().strip()
    

    while user_ip != 'exit':
        print(len(game_deck))    
        if user_ip == 'hit':
            player_tot = 0
            bj_deal(p_hand, game_deck)
            print(f'\nDEALER: | * |{d_hand[1]}\nPLAYER: ', *p_hand, sep = "",)


            player_tot = bj_score(p_hand)
            if player_tot > 21:
                print ('BUSTED YOU LOSE\n♠️ ♣️ ♦️ ♠️ ♥️ ♦️ ♠️ ♥️ ♣️ ♠️ ♥️ ♣️ ♦️')
                # reset game with current deck
                game_deck, d_hand, p_hand = bj_shuffle(game_deck)
                print(f'\nDEALER: | * |{d_hand[1]}\nPLAYER: ', *p_hand, sep = "")
                print('♠️ ♣️ ♦️ ♠️ ♥️ ♦️ ♠️ ♥️ ♣️ ♠️ ♥️ ♣️ ♦️')
                user_ip = input('\nEnter [hit,stay,help,exit]: ').lower().strip()
            #  TODO: Get 21 working
            elif player_tot == 21:
                print ('Player got 21\n♠️ ♣️ ♦️ ♠️ ♥️ ♦️ ♠️ ♥️ ♣️ ♠️ ♥️ ♣️ ♦️')
                game_deck, d_hand, p_hand = bj_shuffle(game_deck)   
                print(f'\nDEALER: | * |{d_hand[1]}\nPLAYER: ', *p_hand, sep = "")
                print('♠️ ♣️ ♦️ ♠️ ♥️ ♦️ ♠️ ♥️ ♣️ ♠️ ♥️ ♣️ ♦️')
                user_ip = input('\nEnter [hit,stay,help,exit]: ').lower().strip()
            else:
                user_ip = input('\nEnter [hit,stay,help,exit]: ').lower().strip()
        # elif user_ip == 'test':
        #     test_hand = ['A ♠️','K ♠️', '2 ♠️']
        #     test_score = bj_score(test_hand)
        #     print(test_score)
        #     user_ip = input('Bad Input...\nEnter [hit,stay,help,exit]: ').lower().strip()
        else:
            user_ip = input('Bad Input...\nEnter [hit,stay,help,exit]: ').lower().strip()



    # print (len(game_deck), d_hand, p_hand, dealer_tot, player_tot)


    # * Testing:
    # for i in range (0,55):
    #     deal(p_hand, game_deck)
    # print( len(game_deck), p_hand, d_hand)



def bj_shuffle(deck):
    # create deck using lists found in variables.py if current deck is empty
    if len(deck) == 0:
        for suit in variables.suits:
            for card in variables.cards:
                deck.append(f'|{ card } { suit }|')
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

def bj_score(target_hand):
    score = 0
    # score calculated by using first char in index item as key for variables.card_val 
    for card in target_hand:
        score += int(variables.card_val[card[1]])
        
    return score

def bj_hint(dealer , player):
    pass




bj_game()
