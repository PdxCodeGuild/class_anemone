#Version 1
#Convert a given number into its english representation

#num = input('Enter a number: ')

from re import T


num = input('Enter a number: ')

#Example: 67

tens_digit = int((num)) // 10
ones_digit = int((num)) % 10

#Result: 6 and 7

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
    10: "ten",


    20 :"twenty-",
    30 : "thirty-",
    40 : "fourty-",
    50 : "fifty-",
    60 : "sixty-",
    70 : "seventy-",
    80 : "eighty-",
    90 : "ninety-",
}

if len(str(num)) == 1:
    print (english_nums[ones_digit])            #prints english word for numbers one through nine



    



# print (tens_digit)
# print (ones_digit)

# print (english_nums[tens_digit] + english_nums[ones_digit])


