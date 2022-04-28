import random




def card():
    return

def draw():
    yes = ['yes', 'yea', 'y', 'hit', 'deal']
    no = ['no', 'na', 'n', 'stay']
    blackj_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    numblackj_deck = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 } 
    hand = []
    total = []
    card = random.choice(blackj_deck)
    hand.append(card)
    print(f'Your first card is a {card}')
    total.append(numblackj_deck[card]) 

    card = random.choice(blackj_deck)
    hand.append(card)
    print(f'Your second card is a {card}')
    total.append(numblackj_deck[card]) 

              
    while sum(total) <= 21:
        deal = input(f'You are at {sum(total)}. Would you like to hit or stay: ').lower()
        if sum(total) == 21:
            status = 'BLACKJACK!'
            print(status)
            return status
        elif deal in no:
            print(f'Staying at {sum(total)}')
            status = 'Should have gone for broke'
            return status
        elif deal in yes:
            card = random.choice(blackj_deck)
            hand.append(card)
            print(f'Your next card is a {card}')
            total.append(numblackj_deck[card])
        else:
            break
    
    if  sum(total) > 21:
        status = 'Busted'
        print(status)
        return status
        


def Lets_Play():
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

game = Lets_Play()

print(game)