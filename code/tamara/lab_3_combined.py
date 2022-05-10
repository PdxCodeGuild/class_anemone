# create directories for the hundreds, tens, ones and teens numbers as keys and the written version of it as values
hundreds_digit_directory = {0: '', 1: 'one hundred ', 2 : 'two hundred ', 3 : 'three hudred ', 4: 'four hundred ', 5: 'five hundred ', 6: 'six hundred ', 7: 'seven hundred ', 8: 'eight hundred ', 9: 'nine hundred '}
tens_digit_directory = {0: '', 1: 'teen', 2: 'twenty ', 3: 'thirty ', 4: 'forty ', 5: 'fifty ', 6: 'sixty ', 7: 'seventy ', 8: 'eighty ', 9: 'ninty '}
ones_digit_directory = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens_directory = {10 : 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 15: 'fifteen'}

# have the user enter a number to be converted and save it as convert_number
convert_number = int(input("Enter a number between 0-999 to have it converted to text "))

# tell the user they didn't enter a valid number if outside 0-999
if convert_number < 0 or convert_number > 999:
    print("That was not a valid entry")

# Isoating the different digits, hundreds, tens and ones so they can be converted, creates seperate teen digit to deal with
# weird naming conventions of teen numbers
else:
    hundred_digit = convert_number // 100
    ones_digit = convert_number%10
    tens_digit = (convert_number // 10) % 10
    teens_digit = f'{tens_digit}{ones_digit}'
    teens_digit = int(teens_digit)

# print statment for zero
if hundred_digit == 0 and teens_digit == 0:
    print(f'zero') 

# create print statement for numbers ending in 10 - 13 and 15 because these have weird illogical names
elif teens_digit > 9 and teens_digit < 14 or teens_digit == 15:
    print(f'{hundreds_digit_directory[hundred_digit]}{teens_directory[teens_digit]}')

# create print statement for the 14-19 teen numbers because teen comes after the ones digit for some reason
elif teens_digit > 13 and teens_digit < 20:
    print(f'{hundreds_digit_directory[hundred_digit]}{ones_digit_directory[ones_digit]}{tens_digit_directory[tens_digit]}')

# for the rest of the normal numbers ending in 0-9 and 20-99, print statement based on userinput. Fishes written version of the number they enter from the directories
else:
    print(f'{hundreds_digit_directory[hundred_digit]}{tens_digit_directory[tens_digit]}{ones_digit_directory[ones_digit]}')
