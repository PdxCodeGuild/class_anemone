

# Convert a Number to Phrase


num = (input('Select any number 0-99: '))

print = (num[0])

ones_digit = (num % 10)
tens_digit = (num // 10)
hundreds_digit = (num // 100)

#print(num)

singles = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

teens = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",    
]

tens = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]


#Single
if len(str(num)) == 1:
    print(singles[ones_digit])

elif len(str(num)) == 2 and num[0] == 1:
    print(teens[tens_digit])

# elif len(str(num)) == 2 and str(num[1]) == 0:
#     print(teens[tens_digit])
