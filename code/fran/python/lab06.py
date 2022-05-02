# Lab06.py - Credit Card Validation
# Fran Kappes

# Collect credit card number from user for validation
credit_card_num = input("Enter a credit card number: ")

print(f"entered cc: {credit_card_num}")


# Convert the string into a list of integers
cc_num_list = []
i = 0

# testing the old way
# while i < len(credit_card_num):
#     cc_num_list.append(int(credit_card_num[i]))

#     i += 1

cc_num_list = [int(credit_card_num[i]) for credit_card_num in credit_card_num]
print(f"credit_card_num_list: {cc_num_list}")


# Strip the last digit (the check digit) and put it in a variable
check_digit = cc_num_list.pop(15)
print(f"check digit: {check_digit}")
print(f"15-digit credit_card_num_list: {cc_num_list}")


# Reverse the remaining 15 digits
cc_num_list.reverse()
print(f"reversed cc num list: {cc_num_list}")


# Double every other element in the reversed list (starting with the first number in the list)
double_cc_num_list = []
#i = 0

#for num in cc_num_list:
# while i < len(cc_num_list):
#     if i%2 ==1:
#         double_cc_num_list.append(num*2)
#     else:
#         double_cc_num_list.append(num)

#     i += 1

#double_cc_num_list = [cc_num_list[i]*2 for num in cc_num_list if i%2 == 1]
double_cc_num_list = [item*2 if index%2 == 0 else item for index,item in enumerate(cc_num_list)]

#print(f"doubled num list: {double_cc_num_list}")
for i,n in enumerate(cc_num_list):
    print(i,n)


# Subtract 9 from numbers that are greater than nine



# Sum all values in the list



# Compare the ones digit of the resulting sum to the check digit. 
#   If the digits match, then the credit card number is valid.


