# Lab03.py - Number to Phrase 
# Fran Kappes

# Define number-to-word conversion dictionary for single digit numbers
number_to_word_ones_digit = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
    }

# Define number-to-word conversion dictionary for 11-19 
number_to_word_teens = {
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
    }

# Define number-to-word conversion dictionary for tens place 
number_to_word_tens_digit = {
    "0": "",
    "1": "ten",
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
    }

# Define number-to-word conversion dictionary for hundreds place 
number_to_word_hundreds_digit = {
    "0": "",
    "1": "one hundred",
    "2": "two hundred",
    "3": "three hundred",
    "4": "four hundred",
    "5": "five hundred",
    "6": "six hundred",
    "7": "seven hundred",
    "8": "eight hundred",
    "9": "nine hundred"
    }

# Prompt user to enter a distance
user_number = int(input("Enter a number: "))

# Convert user_number to a phase

if user_number < 10:
    number_phrase = number_to_word_ones_digit[str(user_number)]
elif 10 < user_number < 20:  # handle teens
    number_phrase = number_to_word_teens[str(user_number)]
elif 110 < user_number < 120:  # handle teens component
    hundreds_digit = user_number//100
    hundreds_phrase = number_to_word_hundreds_digit[str(hundreds_digit)]

    tens_digit = tens_digit = user_number%100
    tens_phrase = number_to_word_teens[str(tens_digit)]

    number_phrase = hundreds_phrase + ' ' + tens_phrase
else:
    # Parse through the number string to find the phrase for each digit
    # Determine hundreds digit and phrase
    hundreds_digit = user_number//100
    hundreds_phrase = number_to_word_hundreds_digit[str(hundreds_digit)]
    
    # Determine the tens and ones digits and corresponding phrases
    if hundreds_digit == 0:  # it is a two-digit number
        tens_digit = user_number//10 
        ones_digit = user_number%10

    else: # number is in the hundreds
        tens_digit = (user_number%100)//10
        ones_digit = (user_number%100)%10

    tens_phrase = number_to_word_tens_digit[str(tens_digit)]
    if ones_digit == 0:
        ones_phrase = ''
    else:
        ones_phrase = number_to_word_ones_digit[str(ones_digit)]

    number_phrase = hundreds_phrase + ' ' + tens_phrase + ' ' + ones_phrase

print(f"""
{number_phrase}
""")