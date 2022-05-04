def creditcard_check(input_numbers): # create the function

    creditcard = [int(number) for number in input_numbers] # turn string of numbers into list of integar numbers called creditcard

    check_digit = creditcard.pop() # remove last number and save it for later to check credit card validity

    creditcard.reverse() # reverses the list

    print(f"These are the card numbers reveresed and with last number removed {creditcard}") # print statement to check functionality can be be removed

    creditcard_multiplied = [] # define empty list for multiplied numbers

    for i, number in enumerate(creditcard): # create for loop that multiplies every other number
        if i % 2 == 0:
            number = number * 2
            creditcard_multiplied.append(number)
        elif i % 2 != 0:
            number = number
            creditcard_multiplied.append(number)

    print(f"These are the card numbers with every other number multiplied by 2 {creditcard_multiplied}") # print statement to check functionality can be be removed

    creditcard_subtracted = [] # define empty list for subtracted numbers

    for number in creditcard_multiplied: # create for loop to subtract 9 from numbers over 9
        if number > 9:
            number = number - 9
            creditcard_subtracted.append(number)
        elif number < 10:
            number = number
            creditcard_subtracted.append(number)

    print(f'These are the card numbers with numbers of 9 having 9 subtracted from them {creditcard_subtracted}') # print statement to check functionality can be be removed

    sum = 0 

    for sums in creditcard_subtracted: # add all the numbers together and put them into the sum variable
        sum = sum + sums

    print(f'this is the sum of the numbers {sum}') # print statement to check functionality can be be removed

    last_sum_digit = sum % 10

    if check_digit == last_sum_digit: # check if the last digit in the sum is the same as last digit of credit card
        print("The credit card number you entered is valid")
    else:
        print("The credit card number you entered is not Valid")

input_numbers = input("Please enter your credit card number: ")

creditcard_check(input_numbers)