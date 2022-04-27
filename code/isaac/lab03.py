'''Number to Phrase'''

# VERSION 1

# Create two lists from 0 to 20 in english
# Ones in one list and tens in another.
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
'eight', 'nine']
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create tens digits.
tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
'seventeen', 'eightteen', 'nineteen']
tens_digits = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Create the rest from 20 up to 100 with base 10
high_digits = ['twenty']
higher_digits = [20]





# Create user input for number and print corresponding position per list
user_input = input("Type a number: ")
user_input = int(user_input)

if user_input in single_digits:
    location_num = single_digits.index(user_input)
    phase_one = ones[location_num].title()
    print(phase_one)

# if user_input in tens_digits:
#     location_num_ten = tens_digits.index(user_input)
#     print(tens[location_num_ten])

if user_input in higher_digits:
    location_high = higher_digits.index(user_input)
    phrase_three = high_digits[location_high].title()
    print(phrase_three)
