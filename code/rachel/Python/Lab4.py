#Lab4
#Basic Blackjack Advice by asking player for two cards

card_one = input("What is your first card? ")
card_two = input("What is your second card? ")
card_three = input("What is your third card? ")

card_values = {

    "A" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,

}

total = (card_values[card_one] + card_values[card_two] + card_values[card_three])

#print (total)

if total < 17:
    print (str(total), "Hit")

elif total >= 17:
    if total > 21:
        print (str(total), "Already Busted")
    if total < 21:
        print (str(total), "Stay")
    if total == 21:
        print (str(total), "Blackjack!")
