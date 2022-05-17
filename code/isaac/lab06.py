'''Credit Card Validation'''
card_number = input("Enter 16 digit card number: ")

list_nums = []
for num in card_number:
    list_nums.append(int(num))
# print(list_nums)

# Convert input string into a list of integers(int)
check_digit = list_nums.pop()
# print(check_digit)
# print(list_nums)
list_nums.reverse() # reverse list
list_nums[0::2] = [2 * num for num in list_nums[0::2]] # double every other number 
print(list_nums)

# # Subtract nine from numbers over nine
under_nine = []
for num in list_nums:
    if num > 9:
        under_nine.append(num - 9)
    else:
        under_nine.append(num)
print(under_nine)

# Sum all numbers
values_sum = sum(under_nine) % 10
print(values_sum)

if values_sum == check_digit:
    print("Card is valid!")
else:
    print("Card invalid")

