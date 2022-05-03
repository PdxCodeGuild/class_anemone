input_numbers = input("Please enter your credit card number: ")

creditcard = [int(number) for number in input_numbers] # turn string of numbers into list of integar numbers called creditcard

check_digit = creditcard.pop() # remove last number and save it for later to check credit card validity

creditcard.reverse() # reverses the list

creditcard_multiplied = [number*2 for i, number in enumerate(creditcard) if i % 2 == 0] # multiply every other number

for i, number in enumerate(creditcard): # add the none multiplied ones back in
    if i % 2 != 0:
        creditcard_multiplied.append(number)

creditcard_minus = [number - 9 for number in creditcard_multiplied if number > 9]

for numb in creditcard_multiplied:
    if numb >= 10:
        creditcard_multiplied.remove(numb)

for numb in creditcard_multiplied:
    if numb >= 10:
        creditcard_multiplied.remove(numb)

for numb in creditcard_multiplied: # I am not sure why but I needed to repeat this loop 3 times to delete all of the numbers over 10 
    if numb >= 10: # would need even more loops for even larger number inputs
        creditcard_multiplied.remove(numb)

print(f'list of multiplied ones at front and none multiplied at back with any 10 or over removed {creditcard_multiplied}')
    
for numbs in creditcard_minus:
    creditcard_multiplied.append(numbs)

sum = 0

for sums in creditcard_multiplied:
    sum = sum + sums

print(f'this is the sum of the numbers {sum}')

check_digit_2 = sum % 10

if check_digit == check_digit_2:
    print("Valid")
else:
    print("Not Valid")