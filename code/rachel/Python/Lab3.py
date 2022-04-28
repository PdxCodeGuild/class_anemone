#Version 1
#Convert a given number into its english representation

from pickle import encode_long
from socketserver import ThreadingUDPServer


num = input('Enter a number: ')

#Example: 67

hundred_digit = int(num) // 100
tens_digit = int(num) // 10
ones_digit = int(num) % 10

# #Result: 6 and 7

english_nums = {
    
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",

    20 :"twenty",
    30 : "thirty",
    40 : "fourty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",

    100 : "one hundred",
    200 : "two hundred",
    300 : "three hundred",
    400 : "four hundred",
    500 : "five hundred",
    600 : "six hundred",
    700 : "seven hundred",
    800 : "eight hundred",
    900 : "nine hundred",
}

if len(str(num)) == 1:
    print (english_nums[ones_digit])            #prints english words for numbers 1 through 9

elif num[0] == "1":
    tens_digit = str(tens_digit) + str(ones_digit)  
    tens_digit = int(tens_digit)
    print (english_nums[tens_digit])            #prints english words for number 11 through 19

elif len(str(num)) == 2 and num[1] == "0":
    tens_digit = int(str(tens_digit) + "0")
    print (english_nums[tens_digit])            #prints english word for numbers 20, 30, 40, etc.

elif len(str(num)) == 2:
    tens_digit = int(str(tens_digit) + "0")
    print (english_nums[tens_digit] + "-" + english_nums[ones_digit])    #prints english words for numbers 21 through 99 (not 20,30,etc.)

elif len(str(num)) == 3 and num[1] == "1":
    hundred_digit = int(str(hundred_digit) + "00")
    tens_digit = str(num[1]) + str(num[2])
    tens_digit = int(tens_digit)
    print (english_nums[hundred_digit], " and " ,english_nums[tens_digit])

elif len(str(num)) == 3 and num[1] == "0" and num[2] == "0":
    hundred_digit = int(str(hundred_digit) + "00")
    print (english_nums[hundred_digit])

elif len(str(num)) == 3 and num[1] == "0":                  
    hundred_digit = int(str(hundred_digit) + "00")          
    print (english_nums[hundred_digit] + " and " + english_nums[ones_digit])

elif len(str(num)) == 3:
    hundred_digit = int(str(hundred_digit) + "00") #400
    hundred_tens_digit = int(num[1] + "0") #50
    ones_digit = int(num[2])
    print (english_nums[hundred_digit], english_nums[hundred_tens_digit] + "-" + english_nums[ones_digit])
    