'''Blackjack Advice'''

# Create a list of number cards and a dictionary of face cards and
# their representing values (face cards only)

number_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
face_cards = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}

# Make a welcome message!
print('''Welcome Blackjack player!  
Here you will be given advice on how to best play the game!\n''')

# Create input for user for a three card draw
card_select = input("Draw first card: ")
card_select += input("Draw second card: ")
card_select += input("Draw third card: ")
card_select = int(card_select)

# 


