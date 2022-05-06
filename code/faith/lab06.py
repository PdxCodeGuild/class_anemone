number = input('Please enter credit card number: ')


def credit_card_validator(number):
    numberlist = []
    numstring = list(number)
    for num in numstring:
        numberlist.append(int(num))
    
    check_number = numberlist.pop()
    numberlist.reverse()
    double_num = []

    for i , num in enumerate(numberlist):
    
        if i % 2 ==0:
                double_num.append( num * 2)
        else:
                double_num.append(num)


    for x in range(len(double_num)):
        if double_num[x] > 9:
            double_num[x] -= 9
    # print(double_num)
            
    result = sum(double_num)
    print(result)


    secdigit = result % 10
    if secdigit == check_number:
        return 'Valid'
    else:
        return 'Invalid'
    
print(credit_card_validator(number))