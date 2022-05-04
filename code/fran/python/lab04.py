# Lab04 - Blackjack Advice
# Fran Kappes
# Programming note: Not including error handling for input values 
#   other than what is requested/expected.


# Create dictionary of card values
card_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

# Collect card info from user
card_1 = input("What's your first card? (2-9,A,K,Q,J): ")
card_2 = input("What's your second card? (2-9,A,K,Q,J): ")
card_3 = input("What's your third card? (2-9,A,K,Q,J): ")

# Add card values and return advice on what to do next
# For version 1, assuming aces are always worth one point
hand_total = card_values[card_1] + card_values[card_2] + card_values[card_3]

# Return advice to user
if hand_total < 17:
    print(f"{hand_total} Hit")
elif 17 <= hand_total < 21:
    print(f"{hand_total} Stay")
elif hand_total == 21:
    print(f"{hand_total} Blackjack!")
else:
    print(f"{hand_total} Already busted")
