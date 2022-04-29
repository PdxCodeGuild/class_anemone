'''Blackjack Advice'''

# Create a list of number cards and a dictionary of face cards and
# their representing values (face cards only)

# List and dictionary containing card values
number_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
face_cards = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}

# Winning number.  All cards drawn must be equal to this number
winningNumber = 21

# Create a function containing the players deck of cards
# return drawn cards and add up all cards drawn
def card_deck(card_one, card_two, card_three):
    return card_one + card_two + card_three

# Make input variables for number_card and face_card    
first_card = input("Draw your first card: ")
second_card = input("Draw your second card: ")
third_card = input("Draw your third and last card: ")

if first_card or second_card or third_card in number_cards:
    cards_total = int(first_card) + int(second_card) + int(third_card)

# Compare cards drawn
if cards_total < 17:
    print(f"{cards_total} Hit")
elif cards_total > 17 and cards_total < winningNumber:
    print(f"{cards_total} Stay")
elif cards_total > winningNumber:
    print(f"{cards_total} Busted!")
elif cards_total == winningNumber:
    print(f"{cards_total} BlackJack!!!")
