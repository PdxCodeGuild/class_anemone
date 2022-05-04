test_cc = '4556737586899855'

def cc_check(cc_number):
    # Convert the input string into list
    cc_number = list(test_cc)
    cc_original = cc_number
    # Slice off last digit, this is check_digit
    check_digit = test_cc[-1]
    cc_number.pop(-1)
    # Reverse the digits
    cc_number.reverse()
    # Double every other element in reversed list stating with first number
    # subtract 9 from numbers over nine
    cc_doubled = cc_number[::2]
    cc_normal = cc_number[1::2]
    for number in cc_doubled:
        number = int(number)*2
        if number > 9:
            number -= 9
        cc_normal.append(number)
    # sum all values
    check_sum = 0
    for number in cc_normal:
        check_sum += int(number)
        
    # take second digit off sum
    # if that matches the check digit whole card number is valid
    num_str = repr(check_sum)
    if check_digit == num_str[-1]:
        return True
    else:
        return False
def main():

    if cc_check(test_cc):
        print('CC Valid')
    else:
        print('CC Not Valid')
main()