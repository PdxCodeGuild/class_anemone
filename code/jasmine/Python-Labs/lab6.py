  ##Credit Card Validator


card_num = []
double_card = []
subtract_nine=[]

## function to validate credit num from input
def credit_card_validator(card_num):

    #user card input 
    card_num = (input('Enter your card number: '))


    # method tried...No results
    # num_list = list(map(int,card_num.split(",")))
    # print(num_list)

    # convert string into a list
    num_list = [int(num) for num in card_num]
    print(num_list)


    ##Slice off last digit (check digit)
    check_digit = num_list.pop()
    print(check_digit)

    ## reverse the list
    num_list.reverse()
    print(num_list)

    ## double the reverse list
  
    for x in num_list:
          double_card.append(x + x)
    print(str(double_card))

    # subtracting 9 from numbers over 9
    subtract_nine=[]
    for x, num in enumerate(double_card):
          if double_card[x] > 9:
                subtract_nine.append(num-9)
          else:
                subtract_nine.append(num)
    print(subtract_nine)

    ## add the sum of card for total value            
    card_total = sum(subtract_nine)
    print(card_total)

    ## take the second digit off the sum and check value
    second_digit = str(card_total)[1]
    print(second_digit)

    ## check if valid 
    if second_digit == check_digit:
          print("Card is Valid")
    else:
          print("Card is Invalid")

# return(card_num)

card_check = credit_card_validator(card_num)
print(card_check)







