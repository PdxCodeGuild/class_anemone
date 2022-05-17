'''
class_anemone
lab 6
Bailey Baker
'''

card = str(input("Please input credit card number: "))


def credit_card_validator(card):
    # Convert the input string into a list of ints
    number = list(card)
    number = [int(i) for i in number]
    # Slice off the last digit.
    check_digit = number.pop()
    # Reverse the digits.
    number.reverse()
    # Double every other element in the reversed list (starting with the first number in the list).
    for i in range(0, len(number), 2):
        number[i]= number[i] * 2
    # Subtract nine from numbers over nine.
    for i in range(len(number)):
        if number[i] > 9:
            number[i] = number[i] - 9
    # Sum all values and take the second digit of that sum.
    total = sum(number) % 10
    if total == check_digit:
        print("True Valid!")
    else:
        print("card number not valid")

card = credit_card_validator(card)