'''Number to Phrase'''

# VERSION 1

# create dictionaries containing number keys and string values
# representing the specified numbers in the ones, teens and tens
ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eightteen',
    19: 'nineteen'
}

tens = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

# ones_digit = user_input[] % 10
# print(ones_digit)
# tens_digit = (user_input // 10) * 10
# print(tens_digit)
# hundreds_digit = user_input // 100
# print(hundreds_digit)
# huns_tens_digit = ((user_input - (hundreds_digit * 100)) // 10) * 10
# print(huns_tens_digit)
# ones_digit = int(str(user_input)[-1])
# tens_digit = int(str(user_input)[-2]) * 10
# hundreds_digit = int(str(user_input)[-3])
user_input = int(input("Enter a number (0-1000): "))

if user_input < 100:
    if user_input in ones:
        ones_digit = int(str(user_input)[-1])
        print(ones[user_input].title())
    elif user_input in teens:
        print(teens[user_input].title())
    elif user_input in tens:
        tens_digit = int(str(user_input)[-2]) * 10
        print(tens[user_input].title())
    else:
        ones_digit = int(str(user_input)[-1])
        tens_digit = int(str(user_input)[-2]) * 10
 
        print(f"{tens[tens_digit]}-{ones[ones_digit]}".capitalize())

elif user_input <= 1000:        # print out numbers below 1000 in the hundreds
    ones_digit = int(str(user_input)[-1])
    teens_digit = int(str(user_input)[1:])  
    tens_digit = int(str(user_input)[-2]) * 10
    hundreds_digit = int(str(user_input)[-3])
    if ones_digit == 0 and tens_digit == 0:
        print(f"{ones[hundreds_digit]}-hundred".capitalize())
    elif tens_digit == 0:
        print(f"{ones[hundreds_digit]}-hundred and {ones[ones_digit]}".capitalize())
    elif tens_digit in tens and ones_digit in ones:
        print(f"{ones[hundreds_digit]}-hundred and {tens[tens_digit]} {ones[ones_digit]}".capitalize())
    elif tens_digit in tens:
        print(f"{ones[hundreds_digit]}-hundred and {tens[tens_digit]}".capitalize()) 
    elif teens_digit in teens:
        print(f"{ones[hundreds_digit]}-hundred and {teens[teens_digit]}".capitalize()) 
    


# testing print statements to check position

# print(hundreds_digit) 
# print(tens_digit) 
# print(ones_digit)
# print(teens_digit)
