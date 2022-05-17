import math
def credit_card(CC):
    holding = []
    last_num = []
    # CC = input('num: ')
    CC = ' '.join(CC).split(' ') # making a a string list and making it spaced
    CC = [int(nums) for nums in CC] # taking the string and hanging it to a valid int
    pop_last = CC.pop(-1) # removing the last int in list
    last_num.append(pop_last)
    cc_copy = CC.copy()
    cc_copy.reverse()
    cc_copy1 = cc_copy[1::2] #[1::2] taking everyother number after the first number [0]
    holding.extend(cc_copy1)
    math = cc_copy[::2]
    math = [nums*2 for nums in math] #taking the postion [::2] every other number and multiplying it by 2 .. num*2 for position in a..
    math = [nums - 9 if nums > 9 else nums for nums in math] # if nums is >10 nums will!! -9 from a ( else statement needed or it wont work )
    holding.extend(math) # using extend to make 1 list not mulitple with append
    value = sum(holding)%10 # taking the remainder ( last number ) to see if it matches last number of the CC 
    cc_valid = value == sum(last_num)
    result = print(f'\n{cc_valid} it is Valid!\n')
    return result


Card_num = input('\nCredit Card Number: ')
credit_card(Card_num)

# 4556737586899855 CC number on lab page for ref