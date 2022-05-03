test_number = '4556737586899855'

def cc_check(cc_number):
    # Convert the input string into list
    cc_number = list(test_number)
    print(f'ORGINAL: { cc_number }')
    #* ORGINAL: ['4', '5', '5', '6', '7', '3', '7', '5', '8', '6', '8', '9', '9', '8', '5', '5']

    # Slice off last digit, this is check_digit
    check_digit = test_number[-1]
    cc_number.pop(-1)
    # Reverse the digits
    cc_number.reverse()
    # Double every other element in reversed list stating with first number
    # subtract 9 from numbers over nine
    # sum all values
    cc_doubled = []
    cc_check = []
    check_sum = 0
    cc_number = map(lambda x : int(x)*2 , cc_number[::2])
        
    # take second digit off sum
    # if that matches the check digit whole card number is valid
    print(cc_number) #* ['5', '8', '9', '9', '8', '6', '8', '5', '7', '3', '7', '6', '5', '5', '4']
    print(cc_doubled, check_sum, check_digit)
 
    # if check_sum:
    #     return print(True)
    # else:
    #     return print(False)

cc_check(test_number)