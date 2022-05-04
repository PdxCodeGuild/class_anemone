import random

cards = '2345678910JQKA'

dealer = []
player = []

dealer_cards1 = random.choice(cards)
dealer_cards2 = random.choice(cards)

print(f"Dealer has a {dealer_cards1} and 'X'.")

if dealer_cards1 == 'J' or 'Q' or 'K' or 'A':
    dealer_value1 = 10
if dealer_cards1 != 'J' or 'Q' or 'K' or 'A':
    dealer_value1 = dealer_cards1
if dealer_cards2 == 'J' or 'Q' or 'K' or 'A':
    dealer_value2 = 10
if dealer_cards2 != 'J' or 'Q' or 'K' or 'A':
    dealer_value2 = dealer_cards2
dealer_total_cards = dealer_cards1 + dealer_cards2

dealer_new_card = []

if dealer_total_cards == 17:
    dealer_new_card = random.choice(cards)
    dealer.append(dealer_new_card)
    if dealer_new_card == 'J' or 'Q' or 'K' or 'A':
        dealer_value3 = 10
    if dealer_new_card != 'J' or 'Q' or 'K' or 'A':
        dealer_value3 = dealer_new_card
    dealer_total_cards = dealer_total_cards + dealer_new_card

player_cards1 = random.choice(cards)
player_cards2 = random.choice(cards)
player_new_card = []

print(f"Your cards are {player_cards1} and {player_cards2}.")

if player_cards1 == 'J' or 'Q' or 'K' or 'A':
    player_value1 = 10
if player_cards1 != 'J' or 'Q' or 'K' or 'A':
    player_value1 = player_cards1
if player_cards2 == 'J' or 'Q' or 'K' or 'A':
    player_value2 = 10
if player_cards2 != 'J' or 'Q' or 'K' or 'A':
    player_value2 = player_cards2
player_total_cards = player_cards1 + player_cards2

choice = str(input("Would you like to to stay or ?  Choose 1 to 'Hit' or 2 to 'Stay': "))

while True:
    if choice == '1':
        player_new_card = random.choice(cards)
    if player_new_card == 'J' or 'Q' or 'K' or 'A':
        player_new_card = 10
    if player_new_card != 'J' or 'Q' or 'K' or 'A':
        player_value3 = player_new_card
    player_total_cards = player_total_cards + player_new_card
    print(f"Your new card is {player_new_card} now have a total of {player_total_cards} from the deck. ")
    if choice != '2':
        print(f"Dealer has {dealer_total_cards} and you have {player_total_cards}.")
    if player_total_cards > 21:
        print("Bust, you lose!")
    if player_total_cards == 21:
        print("BLACKJACK!, YOU WIN! ")
    if dealer_total_cards == player_total_cards:
        print("You tied!")
    if dealer_total_cards < 21 and player_total_cards > dealer_total_cards:
        print("YOU WIN, lol!")
    break
