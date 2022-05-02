firstcard = input('What is your first card?:  ')
secondcard = input('What is your second card?:  ')
thirdcard = input('What is your third card?:  ')

cards = {
    'A':1,
    'J':10,
    'K':10,
    'Q':10,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10
    }
    
fc = cards[firstcard]
sc = cards[secondcard]
tc = cards[thirdcard]

hand = fc+sc+tc

print(hand)

if hand == 21:
    print('Blackjack')
elif hand >= 21:
    print('Already busted')
elif hand <17:
    print('Hit')
elif hand >= 17 and hand < 21:
    print('Stay')




















