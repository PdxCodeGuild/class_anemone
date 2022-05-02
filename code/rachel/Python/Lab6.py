#Lab6
#Write a function which returns whether a credit card num (string) is is valid as a boolean

card_number = input("Enter credit card number (do not use dashes or spaces):")

#_____________________________________________
num_list = []
num_times_2 = []
num_minus_9 = []


def credit_card_validator(number):
    #Convert input into a list of list of ints
    for number in card_number:
        num_list.append(int(number))
     
    #Slice off the last digit (check digit)
    last_digit = num_list.pop()

    #Reverse the digits
    num_list.reverse()
    
    #Double every other element (starting with first number)
    for index, number in enumerate(num_list):
        if (index % 2) == 0:
            number = number * 2
            num_times_2.append(number)
        elif (index % 2) != 0:
            num_times_2.append(number)
            
    for number in num_times_2:
        if number > 9:
            number = number - 9
            num_minus_9.append(number)
        else:
            num_minus_9.append(number)
    
    sum_of_nums = sum(num_minus_9)

    second_digit = sum_of_nums % 10

    if second_digit == last_digit:
        return ("Valid!")
    else:
        return ("Not valid ):")
#________________________________________________

print (credit_card_validator(card_number))



