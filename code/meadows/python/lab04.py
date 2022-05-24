import random
import string
import math

print('BLACK JACK, PICK 3 CARDS RANGING 2-10 OR A = 1, K,Q,J = 10')


card_1 = str(input('Enter 1st card:')).lower()
card_2 = str(input('Enter 2nd card:')).lower()
card_3 = str(input('Enter 3rd card:')).lower()

deck = {'a':1, 'q':10, 'k':10, 'j':10, '2':2, '3':3, '4':4, '5':5,
'6':6, '7':7, '8':8, '9':9, '10':10}

total = (deck[card_1] + deck[card_2] + deck[card_3])
if total in range(0, 17):       
    response = f'{total}..Less then 17 I would HIT'
    print(response)
elif total in range(17, 21):        
    response = f'{total}.. great or equal to 17, i would STAY'
    print(response)
elif total == 21:
    response = f'{total}..you got exactly 21 .. BLACK JACK!'
    print(response)
else:       
    response = f'{total}..over 21 you BUST'
    print(response)

#meow



