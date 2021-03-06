##Define a dictionary of number words 

ones = {0:'zero', 1:'one', 2: 'two', 3: 'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

tens = {0:'', 1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

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
    print(f"{ones[ones_digit]}")
elif user_input <= 99 and user_input >= 20:
    print(f"{tens[tens_digit]}-{ones[ones_digit]}")
elif user_input >= 10 and user_input <= 19:
    print(f"{teens[user_input]}")

elif user_input > 99 and user_input <= 999:
    if tens_digit == 0 and ones_digit == 0:
        print(f"{hundreds[hun_digit]}")
    if tens_digit > 0 and ones_digit == 0:
        print(f"{hundreds[hun_digit]} {tens[tens_digit]}")
    if ones_digit > 0:
        print(f"{hundreds[hun_digit]}{tens[tens_digit]} {ones[ones_digit]}")
    

