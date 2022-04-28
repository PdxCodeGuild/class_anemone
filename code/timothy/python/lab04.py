# ....Lab 04 Version 1
# deck = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

# def blackjack(a, b, c):
#     if a + b + c < 17:
#         print(a + b + c, "Hit")
#     elif a + b + c >= 17 and a + b + c < 21:
#         print(a + b + c, "Stay")
#     elif a + b + c == 21:
#         print(a + b + c, "Blackjack!")
#     elif a + b + c > 21:
#         print(a + b + c, "Busted!")



# first_card = deck[input("What's your first card? ")]
# second_card = deck[input("What's your second card? ")]
# third_card = deck[input("What's your third card? ")]

# blackjack(first_card, second_card, third_card)

# ....Lab 04 (self)-Version 2 w/ function within function. (COMPLETE)
deck = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

def blackjack(a, b, c):
    def addup():
        return a + b + c
    if addup() < 17:
        print(addup(), "Hit")
    elif addup() >= 17 and addup() < 21:
        print(addup(), "Stay")
    elif addup() == 21:
        print(addup(), "Blackjack!")
    elif addup() > 21:
        print(addup(), "Busted!")



first_card = deck[input("What's your first card? ")]
second_card = deck[input("What's your second card? ")]
third_card = deck[input("What's your third card? ")]

blackjack(first_card, second_card, third_card)