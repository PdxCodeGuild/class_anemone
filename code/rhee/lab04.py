import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
dealer_hand = []
player_hand = []


def dealer(deck):
    hand_cards = []
    for i in range(2):
        random.shuffle(deck)
        cards = deck.pop()
        if cards == 11: cards = 'J'
        if cards == 12: cards = 'Q'
        if cards == 13: cards = 'K'
        if cards == 14: cards = 'A'
        hand_cards.append(cards)
    return hand_cards


def total(hand_cards):
    total = 0
    for cards in hand_cards:
        if cards == 'J' or cards == 'Q' or cards == 'K':
            total += 10
        elif cards == 'A':
            total += 1
        else:
            total += cards
    return total


def cards_to_hit(hand_cards):
    cards = deck.pop()
    if cards == 11: cards = 'J'
    if cards == 12: cards = 'Q'
    if cards == 13: cards = 'K'
    if cards == 14: cards = 'A'
    hand_cards.append(cards)
    return hand_cards


def game():
    dealer_hand = dealer(deck)
    player_hand = dealer(deck)
    print(f"The dealer is showing a {dealer_hand[0]}.")
    print(f"You have a {player_hand} for a total of {total(player_hand)}.")
    if total(player_hand) >= 17:
        print(f"You have {total(player_hand)}, you should consider 'stay'. ")
    choice = input("Do you want to 'Stay' or get another card 'Hit'?: ").lower()

    if choice == 'stay':
        while True:
            total(dealer_hand) < 17
            cards_to_hit(dealer_hand)
            print(f"Dealer now has {dealer_hand}.")
            if total(dealer_hand) > 21:
                print("Dealer busts, YOU WIN! ")
                break
            if total(dealer_hand) == 21:
                # results(dealer_hand, player_hand)
                print("BLACKJACK for dealer! ")
                break

    if choice == 'hit':
        while True:
            total(player_hand) < 17
            cards_to_hit(player_hand)
            print(player_hand)
            print(f"Your have {total(player_hand)}.")
            if 17 <= total(player_hand) < 21:
                print(f"You have {total(player_hand)}, you should consider 'stay'. ")
            if total(player_hand) > 21:
                print("YOU BUST! ")
                break
            if total(player_hand) == 21:
                # results(dealer_hand, player_hand)
                print("BLACKJACK! ")
                break
            option = input("Hit again? ('y' or 'n'):")
            if option == 'y':
                continue
            elif option == 'n':
                print(total(player_hand))
                if total(player_hand) > total(dealer_hand):
                    print(f"You WIN! You have {total(player_hand)} and the Dealer has {total(dealer_hand)}. ")
                else:
                    print(f"Dealer WINS! Dealer has {total(dealer_hand)} and you have {total(player_hand)}.")
                break
            elif choice != 'stay' or 'hit':
                print("Can only accept 'stay' or 'hit', Try again. ")


if __name__ == "__main__":
    game()
