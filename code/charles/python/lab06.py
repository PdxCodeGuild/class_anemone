

def validation(verify):                                         # def for converting a 16 digit card number > 
    ccard = verify
    ccardlist = list(ccard)                                     # change to a list  
    ccardpop = int(ccardlist.pop(-1))                           # popping the last digit for later verification
    
    for i in range(0, len(ccardlist)):                          # converting each string in the list to an integer then reversing
        ccardlist[i] = int(ccardlist[i])              
    ccardr = list(reversed(ccardlist))
    
    for i in range(0, int(len(ccardr)/2 + 1)):                  # having i double to target every other integer and double it... 
        ccardr[i *2] = ccardr[i*2] + ccardr[i*2]                # only works on even digit card numbers so 16, 14 12, and so on
    
    for i in range(0, len(ccardr)):                             # for some reason changed back to a string so...
        ccardr[i] = int(ccardr[i])
    
    for i in range(0, len(ccardr)):                             # targeting each int in the list above 9 and subtracting 9
        if ccardr[i] > 9:
            ccardr[i] = int(ccardr[i]) - 9

    validation = int(sum(ccardr) % 10)                          # comparing the second sum digit to the popped number from earlier.
    if validation == ccardpop:
        return(f'{True} Valid')
         
    else: 
        return(f'{False} Invalid')

while True:
    verify = input('Please enter a 16 digit card number to verify: ')
    if int(len(list(verify))) < 16:
        print('Not a valid amount of digits.')
        pass
    else:
        print(validation(verify))
        break