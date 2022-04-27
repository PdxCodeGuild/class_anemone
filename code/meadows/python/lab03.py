import math
import string

ones_dic = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
tens_dic = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty',
7:'seventy', 8:'eighty', 9:'ninety'}
teen_dic = {11:'eleven', 12:'twelve', 13:'thriteen', 14:'fourteen', 15:'fifteen',
16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}


yes = True
while yes:
    player = int(input('Enter a Number: '))
    if player in range(1, 11):
        ones = player%10
        b_ones = ones_dic.get(ones)
        print(b_ones)
    elif player in range(11, 20):
        teens = teen_dic.get(player)
        print(teens)
    elif player in range(20, 100):
        tens = player//10
        a_tens = tens_dic.get(tens)
        ones = player%10
        b_ones = ones_dic.get(ones)
        print(a_tens,'-',b_ones)
    elif player in range(100, 999):
        hundo = player//100
        a_hundo = ones_dic.get(hundo)
        ones = player%10
        b_ones = ones_dic.get(ones)
        tens = player%100//10
        a_tens = tens_dic.get(tens)
        print(a_hundo,'hundred','-', a_tens ,'-',b_ones)
    
    yeah = ['yes', 'y', 'yeh', 'sure', 'si']
    no = ['no','nah','nope', 'nay']
    again = input('check more? ( Yes or No ) : ')
    if again in yeah:
        yes = True    
    else:
        print('BYE!')
        break




    



    