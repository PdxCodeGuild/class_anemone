cards = {
    'A': 1, '2': 2,
    '3': 3, '4': 4,
    '5': 5, '6': 6,
    '7': 7, '8': 8,
    '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}
first_card = cards[input("What is your first card: ")]
second_card = cards[input("What is your second card: ")]
third_card = cards[input("What is your third card: ")]

def advice(first, second, third):
    if first + second + third < 17:
        print(first + second + third, 'Hit')
    elif first + second + third >= 17 and first + second + third < 21:
        print(first + second + third, 'Stay')
    elif first + second + third == 21:
        print(first + second + third, 'Blackjack!')
    elif first + second + third > 21:
        print(first + second + third, 'Busted')

advice(first_card, second_card, third_card)