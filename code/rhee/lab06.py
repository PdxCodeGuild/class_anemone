
# 1. Convert the input string into a list of ints

user_input = input("Please enter a valid card number: ")
# 2. Slice off the last digit. That is the check digit.
card_numbers = list(user_input)

print("cardnumber: ", card_numbers)

print("last number for CC: ", card_numbers.pop())

print("cardnumber: ", card_numbers)

# 3. Reverse the digits.
card_numbers.reverse()
rev_number = card_numbers

print("reverselist: ", rev_number)

#4 Double every other element in the reversed list (starting with the first number in the list).
number = ""
for i in range(len(rev_number)):
    if i % 2 == 0:
        n = int(rev_number[i]) * 2
        print("Multiply every 2nd: ", n)
#5 Subtract nine from numbers over nine.
        if n > 9:
            n = n - 9
            number += str(n)
        else:
            number += str(n)
    else:
        number += rev_number[i]
print(number)

#6 Sum all values.
sum_num = 0
for n in number:
    if n.isdigit():
        sum_num = sum_num + int(n)
print("Sum of all values: ", sum_num)

#7 Take the second digit of that sum.
print("Last digit of value: ", sum_num % 10)

print(card_numbers.pop())

pop_number = int(card_numbers.pop())

print("pop number is: ", pop_number)
#8 If that matches the check digit, the whole card number is valid.
if sum_num % 10 == pop_number:
    print("Valid credit card. ")
else:
    print("Invalid credit card. Please enter another credit card number. ")

