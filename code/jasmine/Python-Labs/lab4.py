
##BlackJack Game
cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'K': 10,
    'Q': 10,
    'J': 10
}

# user = " "
#points = []

while True:
    
    first_card = input("What is your first card: ")
    second_card = input("What is your second card: ")
    third_card = input("What is your third card: ")
    break

points = cards[first_card] + cards[second_card] + cards[third_card]
#print(points)
if points >= 17 and points < 21:
    print(f'You have {points} ! You should stay here!')

if points == 21:
    print(f' You have {points}! Blackjack')

if points > 21:
    print(f'You have {points} ! Busted! You lost..')

if points < 17:
    print("Hit")
    hit_card = int(input("Choose another card: "))
    new_points = hit_card + points
    print(f'You now have {new_points} points')
# new_points = points + hit_card

# if new_points == 21:
#     print(f' You have {points}! Blackjack')

# if new_points > 21:
#     print(f'You have {points} ! Busted! You lost..')



