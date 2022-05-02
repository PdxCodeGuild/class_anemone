# create dictionary with the cards and their values
card_value = {
    'A': 1, 
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    '10' : 10, 
    'J': 10, 
    'Q': 10, 
    'K': 10
    }

# create function for giving blackjack advice with three card inputs from user
def blackjack_counting(first_card, second_card, third_card):
    first_card_value = card_value[first_card]
    second_card_value = card_value[second_card]
    third_card_value = card_value[third_card]
    #convert inputs to an integer and add them together
    total_card_value = int(first_card_value + second_card_value + third_card_value) 
    # deterime what advice to give the player based on total card value
    if total_card_value < 17:
        advice = 'hit'
    elif total_card_value < 21 and total_card_value > 16:
        advice = 'stay'
    elif total_card_value == 21:
        advice = 'Blackjack'
    else:
        advice = 'already busted'
    return print(f'{total_card_value} {advice}!')

# ask the player for the card inputs and run it as the blackjack_counting function       
print("Your card options are A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K")

card_1 = input("What's your first card? ")
card_2 = input("What's your second card? ")
card_3 = input("What's your thrid card? ")

blackjack_counting(card_1, card_2, card_3)