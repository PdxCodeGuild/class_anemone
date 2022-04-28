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
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
    }

# Prompt user to enter a distance
user_number = int(input("Enter a number: "))

# Convert user_number to a phase

if user_number < 10:
    number_phrase = number_to_word_ones_digit[str(user_number)]
elif 10 < user_number < 20:
    number_phrase = number_to_word_teens[str(user_number)]
else:
    # parse through the number string to find the phrase for each digit
    # determine the tens digit:
    tens_digit = user_number//10

    # determine the ones digit:
    ones_digit = user_number%10

    # assemble number phrase
    user_number = str(user_number)
    
    if ones_digit == 0:
        number_phrase = number_to_word_tens_digit[str(tens_digit)]
    else:
        number_phrase = number_to_word_tens_digit[str(tens_digit)] + '-' + number_to_word_ones_digit[str(ones_digit)]

print(f"""
{number_phrase}
""")