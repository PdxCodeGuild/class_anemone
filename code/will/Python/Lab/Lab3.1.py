


x = input('Enter your number. 0-99 supported: ')

tens_digit = int(x)//10
ones_digit = int(x)%10


tens = ['oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

ones = ['oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

if tens_digit <  1: 
    print (tens[0])
elif tens_digit < 2 :
    print (tens[1])
elif tens_digit < 3:
    print (tens[2])
elif tens_digit < 4:
    print (tens[3])
elif tens_digit < 5:
    print (tens[4])
elif tens_digit < 6:
    print (tens[5])
elif tens_digit < 7:
    print (tens[6])
elif tens_digit < 8:
    print (tens[7])
elif tens_digit < 9 :
    print (tens[8])
elif tens_digit < 10:
    print (tens[9])


if ones_digit <  1: 
    print (tens[0])
elif ones_digit < 2 :
    print (tens[1])
elif ones_digit < 3:
    print (tens[2])
elif ones_digit < 4:
    print (tens[3])
elif ones_digit < 5:
    print (tens[4])
elif ones_digit < 6:
    print (tens[5])
elif ones_digit < 7:
    print (tens[6])
elif ones_digit < 8:
    print (tens[7])
elif ones_digit < 9 :
    print (tens[8])
elif ones_digit < 10:
    print (tens[9])

