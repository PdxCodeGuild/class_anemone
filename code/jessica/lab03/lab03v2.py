##Define a dictionary of number words 



number_words_less = {0:'zero', 1:'one', 2: 'two', 3: 'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

tens = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

hundreds = {1:'hundred', 2:'two-hundred', 3:'three-hundred', 4:'four-hundred', 5:'five-hundred', 6:'six-hundred', 7:'seven-hundred', 8:'eight-hundred', 9:'nine-hundred'}

#user input 
user_input = int(input("input a number "))

#user input calculated 
tens_digit = user_input%100//10
ones_digit = user_input%10
hun_digit = user_input%1000//100

#print(tens_digit, ones_digit) /a note to myself 

#if statements with ranges and dictionary [ is user input ]
if user_input <= 9:
    print(f"{number_words_less[ones_digit]}")
elif user_input >= 10 and user_input <= 19:
    print(f"{teens[user_input]}")
#-----------------------------------------------------
elif user_input >= 20 and user_input < 99:
    print(f"{tens[tens_digit]}")
    if user_input[1] == 0:
        print(tens.keys(user_input))
elif user_input > 99 and user_input < 1000:
    print(f"{hundreds[hun_digit]}-{tens[tens_digit]}-{number_words_less[ones_digit]}")

"""
if tens_digit == 0:
    phrase = ones[ones_digit]
elif tens_digit == 1:
    phrase = teens[ones_digit]
elif ones_digit == 0:
    phrase = tens[tens_digit]
elif tens_digit > 1:
    phrase = tens[tens_digit] + '-' + ones[ones_digit]

if hundreds_digit > 0:
    phrase = hundreds[hundreds_digit] + ' and ' + phrase

if ones_digit == 0 and tens_digit == 0:
        phrase = hundreds[hundreds_digit]
"""