import math
import string

ones_dic = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
 7:'seven', 8:'eight', 9:'nine'}

one_ten = {10:'ten',110:'hundred ten',210:'hundred ten',310:'hundred ten',410:'hundred ten',510:'hundred ten',
610:'hundred ten',710:'hundred ten',810:'hundred ten',910:'hundred ten'}

tens_dic = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty',
7:'seventy', 8:'eighty', 9:'ninety'}

teen_dic = {11:'eleven', 12:'twelve', 13:'thriteen', 14:'fourteen', 15:'fifteen',
16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

yes = True 

while yes:

    player = int(input('Enter a Number: '))          
    if player in range(1, 10):
        ones = player%10
        b_ones = ones_dic.get(ones)
        print(b_ones)
    elif player == 10:
        ten = one_ten.get(player)
        print(ten)
    elif player in range(11, 20):
        teens = teen_dic.get(player)
        print(teens)
    elif player in range(20, 100):
        tens = player//10
        a_tens = tens_dic.get(tens)
        ones = player%10
        b_ones = ones_dic.get(ones)
        if ones == 0:
            b_ones = ' '
        print(f'{a_tens}{b_ones}')

    elif player in range(100,110) or player in range(120,200) or player in range(200,210) or player in range(220,300) or player in range(300,310) or player in range(320,400) or player in range(400,410) or player in range(420,500):
        hundo = player//100
        a_hundo = ones_dic.get(hundo)
        ones = player%10
        b_ones = ones_dic.get(ones)
        if ones == 0:
            b_ones = ' '
        tens = player%100//10
        a_tens = tens_dic.get(tens)
        if tens == 0:
            a_tens = ' '
        print(f'{a_hundo} hundred {a_tens} {b_ones}')

    elif player in range(500,510) or player in range(520,600) or player in range(600,610) or player in range(620,700) or player in range(700,710) or player in range(720,800) or player in range(800,810) or player in range(820,900):
        hundo = player//100
        a_hundo = ones_dic.get(hundo)
        ones = player%10
        b_ones = ones_dic.get(ones)
        if ones == 0:
            b_ones = ' '
        tens = player%100//10
        a_tens = tens_dic.get(tens)
        if tens == 0:
            a_tens = ' '
        print(f'{a_hundo} hundred {a_tens} {b_ones}')

    elif player in range(900,910) or player in range(920,1000):
        hundo = player//100
        a_hundo = ones_dic.get(hundo)
        ones = player%10
        b_ones = ones_dic.get(ones)
        if ones == 0:
            b_ones = ' '
        tens = player%100//10
        a_tens = tens_dic.get(tens)
        if tens == 0:
            a_tens = ' '
        print(f'{a_hundo} hundred {a_tens} {b_ones}')

    elif player in range(111,120) or player in range(211,220)or player in range(311,320)or player in range(411,420)or player in range(511,520)or player in range(611,620)or player in range(711,720)or player in range(811,820)or player in range(911,920):
        hundo = player//100
        a_hundo = ones_dic.get(hundo)
        teeny = player%100
        teens = teen_dic.get(teeny)
        print(f'{a_hundo} hundred {teens}')

    elif player == 110 or player == 210 or player == 310 or player == 410 or player == 510 or player == 610 or player == 710 or player == 810 or player == 910:
        hundo = player//100
        a_hundo = ones_dic.get(hundo)
        print(f'{a_hundo} hundred ten')

    
    
    yeah = ['yes', 'y', 'yeh', 'sure', 'si']
    no = ['no','nah','nope', 'nay']
    again = str(input('check more? ( Yes or No ) : '))
    if again in yeah:
        yes = True    
    else:
        print('BYE!')
        break


    