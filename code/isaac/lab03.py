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
high_digits = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
higher_digits = [20, 30, 40, 50, 60, 70, 80, 90]

# Create a list containing numbers 100 - 900 in base 100
hundreds = ['one-hundred', 'two-hundred', 'three-hundred', 'four-hundred', 'five-hundred',
'six-hundred', 'seven-hundred', 'eight-hundred', 'nine-hundred']
hundred_digits = [100, 200, 300, 400, 500, 600, 700, 800, 900]


# Create user input for number and print corresponding position per list
user_input = input("Type a number(0-19): ")
user_input = int(user_input)

if user_input in single_digits:
    location_num = single_digits.index(user_input)
    print(ones[location_num].title())

if user_input in tens_digits:
    location_num_ten = tens_digits.index(user_input)
    print(tens[location_num_ten].title())

if user_input in higher_digits:
    location_high = higher_digits.index(user_input)
    print(high_digits[location_high].title())

# Create first and second input and combine both numbers
# and print out the phrase for said number
# ex (first number: 20, second number: 1 = Twenty-one)
tens_number = input("Enter first number(20-90 in base 10): ")
tens_number = int(tens_number)
ones_number = input("Enter second number(ones): ")
ones_number = int(ones_number)

if tens_number in higher_digits:
    first_combine = higher_digits.index(tens_number)

if ones_number in single_digits:
    second_combine = single_digits.index(ones_number)

print("{}-{}".format(high_digits[first_combine].title(), ones[second_combine]))

# Now create the same inputs as above but this time with 100 to 900
# Input numbers 100 to 119

hundreds_number = input("Enter hundreds number: ")
hundreds_number = int(hundreds_number)
tens_number = input("Enter tens number: ")
tens_number = int(tens_number)

if hundreds_number in hundred_digits:
    first_combine = hundred_digits.index(hundreds_number)

if tens_number in tens_digits:
    second_combine = tens_digits.index(tens_number)

print("{}-{}".format(hundreds[first_combine].title(), tens[second_combine].title()))

# Now input numbers from 120 and so on.
hundreds_number = input("Enter hundreds number: ")
hundreds_number = int(hundreds_number)
high_numbers = input("Enter 20 or above number: ")
high_numbers = int(high_numbers)
ones_number = input("Enter single digit number: ")
ones_number = int(ones_number)

if hundreds_number in hundred_digits:
    loc_hundred = hundred_digits.index(hundreds_number)

if high_numbers in higher_digits:
    loc_high = higher_digits.index(high_numbers)

if ones_number in single_digits:
    loc_single = single_digits.index(ones_number)

print("{}-{}-{}".format(hundreds[loc_hundred].title(), high_digits[loc_high], ones[loc_single]))
