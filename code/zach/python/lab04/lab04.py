import dealer
import variables

def bj_game(play_game):
    
    game_deck = dealer.build_deck()
    deal_count = 0
    hand_count = 0

    while deal_count < 52:
        bj_deal(game_deck,deal_count, hand_count)



    return print('done')

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
        for i in [card_deck[0],card_deck[2]]:
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
        


def main():
        play_game = input('Would you like to learn to play ♠️ ♥️ ♣️ ♦️ BlackJack ♠️ ♥️ ♣️ ♦️ [Y/n] ').upper().strip()
        bj_game(play_game)

main()
