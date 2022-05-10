import random
import string
import math
#-----------------------------------------------------------ORIGINAL VERSION------------------------------------------------------------------#

# def rando(numbers):
#     hand = []                                     # taking letters[] and appending  and using .extend to make numbers part of the list 
#     letters = ['a', 'q', 'j', 'k']   # taking 
#     letters[0] = 1
#     hand.append(letters[0])
#     letters[1] = 10
#     hand.append(letters[1])
#     letters[2] = 10
#     hand.append(letters[2])
#     letters[3] = 10                     #taking the apendix of "letters" and making each one = their own value
#     hand.append(letters[3])
#     nums = [2,3,4,5,6,7,8,9,10]      
#     hand.extend(nums)
#     random.shuffle(hand)
#     hand = hand*4                         # multiplying the hand = [] by 4 to equal a deck of cards ( for random.shuffle )
#     grave_yard = []
#     for i in range(3):                      # making my list loop 3 times and only picking 3 random numbers out of the 52
#         random.randint(0,len(hand)-1)
#         #grave_yard = hand.pop(random.randint(0,len(hand)-1))
#         grave_yard.append(hand.pop(random.randint(0,len(hand)-1)))  # popping the random.randint and sending it to GY to remove from list of 52 
#     print(grave_yard)
#     return [grave_yard, hand] # returns my graveyard as my hand so i know what i took ( popped) from my random.randint

# def dealer(total):                 # created a function to run through my graveyard ( current hand ) to tell you to stay , hit or you busted
#     if total in range(0, 18):       
#         response = f'{total} I would HIT'
#     elif total in range(18, 21):        
#         response = f'{total} i would STAY'
#     elif total == 21:
#         response = f'{total}..BLACK JACK!'
#     else:       
#         response = f'{total}.. BUST'
#     return response

# results = rando(1) # taking the results of def(rando(numbers)) for use outside of just function
# grave_yard = results[0] # using the result of my grave yard to use a with my def dealer(total)
# cards = sum(grave_yard) # sums up my hand (graveyard)
# print(dealer(cards)) # takes the now sum and gives dealer(total) a reason to respond if it falls in the range


#-----------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------- FIXED VERSION FOR INPUTS -----------------------------------------------------------#

print('BLACK JACK, PICK 3 CARDS RANGING 2-10 OR A = 1, K,Q,J = 10')


card_1 = str(input('Enter 1st card:')).lower()
card_2 = str(input('Enter 2nd card:')).lower()
card_3 = str(input('Enter 3rd card:')).lower()

deck = {'a':1, 'q':10, 'k':10, 'j':10, '2':2, '3':3, '4':4, '5':5,
'6':6, '7':7, '8':8, '9':9, '10':10}

total = (deck[card_1] + deck[card_2] + deck[card_3])
if total in range(0, 18):       
    response = f'{total} I would HIT'
    print(response)
elif total in range(18, 21):        
    response = f'{total} i would STAY'
    print(response)
elif total == 21:
    response = f'{total}..BLACK JACK!'
    print(response)
else:       
    response = f'{total}.. BUST'
    print(response)



