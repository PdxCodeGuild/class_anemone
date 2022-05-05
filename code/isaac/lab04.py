'''Blackjack Advice'''
# Create a list of number cards and a dictionary of face cards and
# their representing values (face cards only)
# Dictionary containing card values
player_deck = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
'7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
}

# Winning number.  All cards drawn must be equal to this number
# lowestDraw for reference
winningNumber = 21
lowestDraw = 17

# Make input variables for number_card and face_card    
first_card = input("Draw your first card: ")
second_card = input("Draw your second card: ")
third_card = input("Draw your third and last card: ")

# Create a function containing the players deck of cards
# return drawn cards and add up all cards drawn
def card_deck(card_one, card_two, card_three):
    return player_deck[card_one] + player_deck[card_two] + player_deck[card_three]

# Sum up all cards drawn from player deck
cards_total = card_deck(first_card, second_card, third_card)
if cards_total in player_deck:
    print(cards_total)

# Compare cards drawn and display hit, stay, blackjack or bust.
if cards_total <= lowestDraw:
    print(f"{cards_total} Hit")
elif cards_total >= lowestDraw and cards_total <= winningNumber:
    print(f"{cards_total} Stay")
elif cards_total > winningNumber:
    print(f"{cards_total} Busted!")
elif cards_total == winningNumber:
    print(f"{cards_total} BlackJack!!!")
