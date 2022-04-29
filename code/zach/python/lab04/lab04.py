import dealer
import variables

def bj_game(play_game):
    deal_count = 0
    game_deck = dealer.build_deck()
    

    bj_deal(game_deck, deal_count)



    return print('done')

def bj_deal(game_deck, deal_count):
    hit = 'H'
    deck_list = []
    while hit == 'H' and deal_count < 52:
        player_hand
        if deal_count <= 48:
            print(deal_count)
            deal_count += 4
        hit = input('h or s').upper()
        
    print(deal_count)

def main():
        play_game = input('Would you like to learn to play ♠️♥️♣️♦️BlackJack♠️♥️♣️♦️?[Y/n] ').upper().strip()
        bj_trainer(play_game)

main()
