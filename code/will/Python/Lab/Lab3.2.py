


x = input('Enter your number. 0-999 supported: ')

hundreds_digit = int(x)//100
tens_digit = (int(x)//10)%10
ones_digit = int(x)%10

hundreds = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

tens = ['oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

ones = ['oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

phrase = []

if hundreds_digit <  1: 
     phrase.append(hundreds[0])
elif hundreds_digit < 2 :
    phrase.append(hundreds[1])
elif hundreds_digit < 3:
    phrase.append(hundreds[2])
elif hundreds_digit < 4:
    phrase.append(hundreds[3])
elif hundreds_digit < 5:
    phrase.append(hundreds[4])
elif hundreds_digit < 6:
    phrase.append(hundreds[5])
elif hundreds_digit < 7:
    phrase.append(hundreds[6])
elif hundreds_digit < 8:
    phrase.append(hundreds[7])
elif hundreds_digit < 9 :
    phrase.append(hundreds[8])
elif hundreds_digit < 10:
    phrase.append(hundreds[9])




if tens_digit <  1: 
     phrase.append(tens[0])
elif tens_digit < 2 :
    phrase.append(tens[1])
elif tens_digit < 3:
    phrase.append(tens[2])
elif tens_digit < 4:
    phrase.append(tens[3])
elif tens_digit < 5:
    phrase.append(tens[4])
elif tens_digit < 6:
    phrase.append(tens[5])
elif tens_digit < 7:
    phrase.append(tens[6])
elif tens_digit < 8:
    phrase.append(tens[7])
elif tens_digit < 9 :
    phrase.append(tens[8])
elif tens_digit < 10:
    phrase.append(tens[9])


if ones_digit <  1: 
     phrase.append(ones[0])
elif ones_digit < 2 :
    phrase.append(ones[1])
elif ones_digit < 3:
    phrase.append(ones[2])
elif ones_digit < 4:
    phrase.append(ones[3])
elif ones_digit < 5:
    phrase.append(ones[4])
elif ones_digit < 6:
    phrase.append(ones[5])
elif ones_digit < 7:
    phrase.append(ones[6])
elif ones_digit < 8:
    phrase.append(ones[7])
elif ones_digit < 9 :
    phrase.append(ones[8])
elif ones_digit < 10:
    phrase.append(ones[9])




print(phrase)