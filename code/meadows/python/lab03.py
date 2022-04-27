import math
import string

roman_ones = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI',
 7:'VII', 8:'VIII', 9:'IX', 10:'X'}
roman_tens = {2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX',
7:'LXX', 8:'LXXX', 9:'XC'}
roman_teens = {11:'XI', 12:'XII', 13:'XIII', 14:'XIV', 15:'XV',
16:'XVI', 17:'XVII', 18:'XVIII', 19:'XIX'}
roman_hundreds = {1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC',
 7:'DCC', 8:'DCCC', 9:'CM', 10:'M'}


yes = True
while yes:
    player = int(input('Enter a Number: '))
    if player in range(1, 11):
        ones = player%10
        b_ones = roman_ones.get(ones)
        print(b_ones)
    elif player in range(11, 20):
        teens = roman_teens.get(player)
        print(teens)
    elif player in range(20, 100):
        tens = player//10
        a_tens = roman_tens.get(tens)
        ones = player%10
        b_ones = roman_ones.get(ones)
        print(f'{a_tens}{b_ones}')
    elif player in range(100, 999):
        hundo = player//100
        a_hundo = roman_hundreds.get(hundo)
        ones = player%10
        b_ones = roman_ones.get(ones)
        tens = player%100//10
        a_tens = roman_tens.get(tens)
        print(f'{a_hundo}{b_ones}{a_tens}')
    
    yeah = ['yes', 'y', 'yeh', 'sure', 'si']
    no = ['no','nah','nope', 'nay']
    again = str(input('check more? ( Yes or No ) : '))
    if again in yeah:
        yes = True    
    else:
        print('BYE!')
        break




    



    