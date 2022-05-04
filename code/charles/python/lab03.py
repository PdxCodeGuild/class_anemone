import random
from string import digits



num_to_text = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 
10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}


x = int(input('Please enter a number between 1 and 999: '))
# print(x)

# print(f'{x in range(0, 99)}')


if x in range(11, 20):
    teenref = num_to_text[x]
    print(teenref)

elif x in range(0, 99):
    tens = x // 10 * 10
    ones = x % 10
    tref = num_to_text[tens]
    oref = num_to_text[ones]
    if ones == 0:
        print(tref)
    elif tens == 0:                                     # added a tens ref to get rid of the ones returning zero
        print (oref)
    else:
        print(f'{tref}-{oref}')
 

elif x in range(100, 999):
    huns = x // 100
    tens = (x - huns * 100) // 10 * 10
    teens = (x - huns * 100)                            # add another teens ref 
    ones = x % 10
    href = num_to_text[huns]                            # assigned as ones and not huns
    tnref = num_to_text[teens]                          #dictionary ref for teens
    tref = num_to_text[tens]
    oref = num_to_text[ones]
    if ones == 0 and tens == 0:                         # add double true statment to get rid of the zero hundred and zero...
        print(f'{href}-hundred')          
    elif tens == 0:
        print(f'{href}-hundred and {oref}')
    elif teens in range(11, 20):
        print(f'{href}-hundred and {tnref}')            # new if statement to pull the teens out
    elif ones == 0: 
        print(f'{href}-hundred and {tref}')
    else:
        print(f'{href}-hundred and {tref}-{oref}')

