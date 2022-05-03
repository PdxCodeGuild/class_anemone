'''
class_anemone
Lab 3
Baiely Baker
'''
# Dictionaries to be used as a key to find correct output
nums_dict1 = {
   0: '',
   1: 'one',
   2: 'two',
   3: 'three',
   4: 'four',
   5: 'five',
   6: 'six',
   7: 'seven',
   8: 'eight',
   9: 'nine',
}
nums_dict2 = {
   10: 'ten',
   11: 'eleven',
   12: 'twelve',
   13: 'thriteen',
   14: 'fourteen',
   15: 'fifteen',
   16: 'sixteen',
   17: 'seventeen',
   18: 'eighteen',
   19: 'nineteen',
}
nums_dict_tens2 = {
   0: 'ten',
   1: 'eleven',
   2: 'twelve',
   3: 'thriteen',
   4: 'fourteen',
   5: 'fifteen',
   6: 'sixteen',
   7: 'seventeen',
   8: 'eighteen',
   9: 'nineteen',
}
nums_dict3 = {
   0: '',
   1: 'ten',
   2: 'twenty',
   3: 'thirty',
   4: 'fourty',
   5: 'fifty',
   6: 'sixty',
   7: 'seventy',
   8: 'eighty',
   9: 'ninety',
 }
nums_dict4 = {
    1: 'hundred',
    2: 'two-hundred',
    3: 'three-hundred',
    4: 'four-hundred',
    5: 'five-hundred',
    6: 'six-hundred',
    7: 'seven-hundred',
    8: 'eight-hundred',
    9: 'nine-hundred',
}

#Get input from user.
num = int(input("Enter a number between 0-999: "))
#Finds the correct number to be used when looking through respective dictionary. 
hundreds_digit = num // 100
tens_digit = num % 100 // 10
ones_digit = num % 10

#If statements used to ensure correct dictionaries and print statements are output depending on number input by user.
if num == 0:
    print('zero')
elif num <= 9:
    print(nums_dict1[num])
elif num <= 19:
    print(nums_dict2[num])
elif num <= 99:
    print(nums_dict3[tens_digit] + ' '+  nums_dict1[ones_digit])
elif num <= 999 and tens_digit == 1:
    print(nums_dict4[hundreds_digit]  + ' ' + nums_dict_tens2[ones_digit])
elif num <= 999 and tens_digit != 1:
    print(nums_dict4[hundreds_digit]  + ' ' + nums_dict3[tens_digit]  + ' ' +  nums_dict1[ones_digit])


