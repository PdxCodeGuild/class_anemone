


x = int(input('Enter your number. 0-999 supported: '))

hundreds_digit = x // 100
tens_digit = x % 100 // 10
ones_digit = x % 10

hundreds = {1:'hundred', 2:'two hundred', 3:'three hundred', 4:'four hundred', 5:'five hundred', 6:'six hundred', 7:'seven hundred', 8:'eight hundred', 9:'nine hundred', }

tens = {0:' ',1:'ten', 2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

ones_2 = {10:'ten', 11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

ones = {0:' ', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

if x == 0:
    print('Zero')
elif x <= 9:
    print(ones[x])
elif x <= 19:
    print(ones_2[x])
elif x <= 99:
    print(tens[tens_digit]+ ' ' + ones[ones_digit])
elif x <= 999 and tens_digit == 1:
    print(hundreds[hundreds_digit] + ' ' + ones_2[x - (hundreds_digit *100)])
elif x <= 999 and tens_digit != 1:
    print(hundreds[hundreds_digit] + ' ' + tens[tens_digit] + ' ' + ones[ones_digit])





#I think this is complete.