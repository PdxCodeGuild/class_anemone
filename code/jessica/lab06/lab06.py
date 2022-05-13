#Step 1 convert string to list in a function

user_input = input('Enter your credit card number ')

credit_card_list = [int(num) for num in user_input]
print(credit_card_list)

##Slice off check digit
check_digit = credit_card_list.pop()
print(check_digit) #5


# #Reverse car list
credit_card_list.reverse()
print(credit_card_list)

##Double every other number                       
double_card = [2*n if i%2 == 0 else n for i,n in enumerate(credit_card_list)] 
# double_card = []
# for i,num in enumerate(credit_card_list):
#     if i%2 == 0:
#         double_card.append(2*num)
#     else:
#         double_card.append(num)

print(double_card)

over_nine = []
for i,num in enumerate(double_card):
    if num > 9:
        over_nine.append(num-9)
    else:
        over_nine.append(num)

print(over_nine)

sum_of_nums = sum(over_nine)

print(sum_of_nums)

check_value = str(sum_of_nums)[1] #5
print(check_value)


#str cannot be equal to an int. I needed to convert the check value back to int. 
if check_digit == int(check_value):
    print('Valid card')
else:
    print('Try Again')

