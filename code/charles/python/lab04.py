import random




def draw():
    yes = ['yes', 'yea', 'y', 'hit', 'deal']
    no = ['no', 'na', 'n', 'stay']
    blackj_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] # dict for letters
    numblackj_deck = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 } #dict for letter numbers
    hand = [] # players current hand 
    total = [] # num list of cards in hand
    card = random.choice(blackj_deck)
    hand.append(card)
    print(f'Your first card is a {card}')
    total.append(numblackj_deck[card]) 

    card = random.choice(blackj_deck)
    hand.append(card)
    print(f'Your second card is a {card}')
    total.append(numblackj_deck[card])     #drawing of players first two cards

     

    while sum(total) < 21: # while loop to add cards to hand til bust or stay
        
        stay = f'{(" " .join(hand))} You are at {sum(total)}. You should Stay but would you like to hit.'
        less = f'{(" " .join(hand))} You are at {sum(total)}. You should Hit.'

        if sum(total) < 17:
            print({less})
            deal = input('Hit or Stay: ').lower()
            if deal in no:
                break
            elif deal in yes:
                card = random.choice(blackj_deck)
                hand.append(card)
                print(f'Your next card is a {card}')
                total.append(numblackj_deck[card])
            else:
                break
        
        elif sum(total) >= 17 and sum(total) < 21:          # add if/elif for advising hit and stay at the appropriate card values
            print({stay})
            deal = input('Hit or Stay: ').lower()

            if deal in no:
                break
            elif deal in yes:
                card = random.choice(blackj_deck)
                hand.append(card)
                print(f'Your next card is a {card}')
                total.append(numblackj_deck[card])
            else:
                break
    
    if  sum(total) > 21:               # if/elif for based of sum of total
        status = 'Busted'
        print(sum(total), status)
        return status
    elif sum(total) == 21:
        status = 'BLACKJACK!'
        print(sum(total), status)
        return status
    elif sum(total) < 21:
        print(f'Staying at {sum(total)}')
        status = 'Should have gone for broke'
        return status
        


def Lets_Play():          # black jack initilizer
    play = True
    yes = ['yes', 'yea', 'y']
    no = ['no', 'na', 'n']
    
    while play:
        okay = input('Would you like to paly Black Jack? Enter yes or no: ').lower()
        if okay in no:
            play == False
            break
        elif okay in yes:
            status = draw()
            return status

Lets_Play()