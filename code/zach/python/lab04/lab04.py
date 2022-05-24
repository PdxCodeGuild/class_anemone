import dealer
import variables

#TODO: not working properly yet will come back
def bj_game(play_game):

    game_deck = dealer.build_deck()
    deal_count = 0
    hand_count = 0

    while deal_count < 52:
        bj_deal(game_deck, deal_count, hand_count)

    return print('done')

#TODO: not working properly yet will come back
def bj_deal(game_deck, deal_count, hand_count):
    card_deck = list(game_deck.keys())
    card_value = list(game_deck.values())

    deal_count = 0
    hit = 'H'
    player = []
    player_val = 0
    dealer = []
    dealer_val = 0

    # first deal will be unique in that it is a total of 4 cards alternating between player and dealer for fairness.
    if deal_count == 0:
        for i in [card_deck[0], card_deck[2]]:
            player.append(i)
        for j in [card_deck[1], card_deck[3]]:
            dealer.append(j)

        # dealer_val = dealer_val + card_value[1]) + int(card_value[3])
        deal_count += 4
        # for card in player:
        #     player_val += game_deck[card]
    # elif deal_count == 4:
    else:
        player.append(card_deck[deal_count])
        # for card in player:
        #     player_val += game_deck[card_deck[deal_count]]
        deal_count += 1

        print(dealer, player, player_val)
        hit = input('h or s').upper()

# bj_hint function fulfills the requirement for lab04, the goal of implementing the function this way is to allow the user to eventually be able to prompt a hint at anytime during the game the game by attaching it to some input
def bj_hint(player_hand):

    separator = ' , '
    print(f'Your current hand is { separator.join(player_hand) }')
    card_val = input('enter next card (2-A)').strip().upper()
    player_hand.append(card_val)
    hand_val = 0

    for card in player_hand:
        hand_val += variables.card_val[card[0]]
    if hand_val < 17:
        return print(f'Your hand is { separator.join(player_hand) }  with a value of { hand_val }\nPLAYER SHOULD HIT')
    elif 17 <= hand_val < 21: 
        return print(f'Your hand is { separator.join(player_hand) }  with a value of { hand_val }\nPLAYER SHOULD STAY')
    elif hand_val == 21:
        return print(f'Your hand is { separator.join(player_hand) }  with a value of { hand_val }\nPLAYER HAS BLACKJACK')
    else:
        return print(f'Your hand is { separator.join(player_hand) }  with a value of { hand_val }\nPLAYER HAS ALREADY BUSTED')

def main():
    play_game = input(
        'Would you like to learn to play ♠️ ♥️ ♣️ ♦️ BlackJack ♠️ ♥️ ♣️ ♦️ [Y/n] ').upper().strip()
    test_hand = ['7 ♥️', '9 ♠️'] # Change to see different results from game functions by hand.

    bj_hint(test_hand)

if __name__ == '__main__':
    main()
