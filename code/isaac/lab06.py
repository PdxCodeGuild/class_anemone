'''Credit Card Validation'''
card_number = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]

# Convert input string into a list of integers(int)
def credit_card_validator():
    other_number = card_number
    other_number.reverse() # reverse list
    doubled_number = [2 * x for x in other_number[::2]] # double every other number
    print(other_number)
    print(doubled_number)

credit_card_validator()