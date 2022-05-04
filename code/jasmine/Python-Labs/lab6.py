  ##Credit Card Validator
card_num = []
numbers = []

def credit_card_validator(card_num):
   
    card_num = (input('Enter your card number: '))

    num_list = list(map(int,card_num.split(",")))
    print(num_list)

    check_digit = num_list.pop()
    print(check_digit)

    # check_digit.reverse()
    # print(num_list)

    return(card_num)

card_check = credit_card_validator(card_num)
print(card_check)







