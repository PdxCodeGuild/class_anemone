

# Convert a Number to Phrase

## IN PROGRESS

num = int(input('Select any number 0-99: '))

#print = (num[0])

ones_digit = (num % 10)
tens_digit = (num % 100 // 10)
hundreds_digit = (num % 1000 // 100)

#print(num)

singles = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
}

teens = {
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",    
}

tens = {
    0: "",
    1: "ten",
    2:"twenty",
    3:"thirty",
    4:"forty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety"
}


hundreds = {
    1:'hundred', 
    2:'two-hundred', 
    3:'three-hundred', 
    4:'four-hundred', 
    5:'five-hundred', 
    6:'six-hundred', 
    7:'seven-hundred', 
    8:'eight-hundred', 
    9:'nine-hundred'}


#Single
if num <= 9:
    print(singles[ones_digit])

#Teens
elif num >= 10 and num <= 19:
    print(f'{teens[num]}')

#Tens
elif num >=20 and num <= 99:
    if ones_digit != 0:
        print(f'{tens[tens_digit]} - {singles[ones_digit]}')
    else:
        print(f'{tens[tens_digit]}')


elif num >= 100:
    if tens_digit == 0 and ones_digit == 0:
        print(f"{hundreds[hundreds_digit]}")
    elif ones_digit != 0:
        print(f"{hundreds[hundreds_digit]} {tens[tens_digit]} {singles[ones_digit]}")
    elif ones_digit == 0:
        print(f"{hundreds[hundreds_digit]} {tens[tens_digit]}")

# if num <= 9:
#     print(f"{singles[ones_digit]}")
# elif num <= 99 and num >= 20:
#     print(f"{tens[tens_digit]}-{singles[ones_digit]}")
# elif num >= 10 and num <= 19:
#     print(f"{teens[num]}")

# elif num > 99 and  num <= 999:
#     if tens_digit == 0 and ones_digit == 0:
#         print(f"{hundreds[hundreds_digit]}")
#     if tens_digit > 0 and ones_digit == 0:
#         print(f"{hundreds[hundreds_digit]} {tens[tens_digit]}")
#     if ones_digit > 0:
#         print(f"{hundreds[hundreds_digit]}{tens[tens_digit]} {singles[ones_digit]}")