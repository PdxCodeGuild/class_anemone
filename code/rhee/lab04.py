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


def results(dealer_hand, player_hand):
    print(f"The dealer has a {dealer_hand} for a total of {total(dealer_hand)},")
    print(f"You have a {player_hand} for a total of {total(player_hand)}.")


def black_jack(dealer_hand, player_hand):
    if total(player_hand) < total(dealer_hand):
        # results(player_hand, dealer_hand)
        print(f"You Lost! \nDealer has {dealer_hand} and you have {player_hand}.")
    elif total(player_hand) > total(dealer_hand):
        # results(player_hand, dealer_hand)
        print(f"You Win! \nYour score is {player_hand} and the dealer has {dealer_hand}.")
    elif total(player_hand) == dealer_hand:
        print(f"It's a tie. You have {player_hand} and the dealer has {dealer_hand}")


def game():
    choice = 0
    dealer_hand = dealer(deck)
    player_hand = dealer(deck)
    print(f"The dealer is showing a {dealer_hand[0]}.")
    print(f"You have a {player_hand} for a total of {total(player_hand)}.")
    choice = input("Do you want to 'Stay' or get another card 'Hit'?: ").lower()
    if choice == 'stay':
        black_jack(dealer_hand, player_hand)
        if total(dealer_hand) < 17:
            cards_to_hit(dealer_hand)
            print(f"Dealer has now has {dealer_hand}.")
        if total(dealer_hand) > 21:
            print("Dealer busts, YOU WIN! ")
            # black_jack(dealer_hand, player_hand)
        if total(dealer_hand) == 21:
            # results(dealer_hand, player_hand)
            print("BLACKJACK for dealer! ")

    elif choice == 'hit':
        cards_to_hit(player_hand)
        print(player_hand)
        if total(player_hand) > 21:
            print("YOU BUST! ")
            if total(player_hand) < 21:
                cards_to_hit(player_hand)
                print(player_hand)
                print(f"Your have: {total(player_hand)}.")
                black_jack(dealer_hand, player_hand)
            if total(player_hand) == 21:
                # results(dealer_hand, player_hand)
                print("BLACKJACK! ")
    else:
        print("Can only accept 'stay' or 'hit'. ")


if __name__ == "__main__":
    game()
