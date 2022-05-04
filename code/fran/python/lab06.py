# Lab06.py - Credit Card Validation
# Fran Kappes

# Collect credit card number from user for validation
credit_card_num = input("Enter a credit card number: ")

#print(f"entered cc: {credit_card_num}")   ### TEST


# Convert the string into a list of integers
cc_num_list = []
i = 0

cc_num_list = [int(credit_card_num[i]) for credit_card_num in credit_card_num]

#print(f"credit_card_num_list: {cc_num_list}")   ### TEST


# Strip the last digit (the check digit) and put it in a variable
check_digit = cc_num_list.pop(15)

#print(f"check digit: {check_digit}")   ### TEST
#print(f"15-digit credit_card_num_list: {cc_num_list}")   ### TEST


# Reverse the remaining 15 digits
cc_num_list.reverse()

#print(f"reversed cc num list: {cc_num_list}")   ### TEST


# Double every other element in the reversed list (starting with the first number in the list)
double_cc_num_list = []

double_cc_num_list = [item*2 if index%2 == 0 else item for index,item in enumerate(cc_num_list)]

#print(f"doubled num list: {double_cc_num_list}")   ### TEST

# TEST enumerate
# for i,n in enumerate(cc_num_list):
#     print(i,n)
# END TEST enumerate


# Subtract 9 from numbers that are greater than nine
subtract_9_list = []

subtract_9_list = [item-9 if item>9 else item for item in double_cc_num_list]

#print(f"after subtracting 9: {subtract_9_list}")   ### TEST


# Sum all values in the list
cc_list_sum = sum(subtract_9_list)

#print(f"cc list sum: {cc_list_sum}")   ### TEST


# Compare the ones digit of the resulting sum to the check digit. 
#   If the digits match, then the credit card number is valid.
sum_ones_place = int(str(cc_list_sum)[-1])

#print(f"sum ones place: {sum_ones_place}")   ### TEST

if check_digit == sum_ones_place:
    print('Valid credit card')
else:
    print('Invalid credit card')
