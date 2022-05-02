

def validation(verify):
    ccard = verify
    ccardlist = list(ccard)
    ccardpop = int(ccardlist.pop(-1))
    
    for i in range(0, len(ccardlist)):
        ccardlist[i] = int(ccardlist[i])
    ccardr = list(reversed(ccardlist))
    
    for i in range(0, int(len(ccardr)/2 + 1)):
        ccardr[i *2] = ccardr[i*2] + ccardr[i*2]
    
    for i in range(0, len(ccardr)):
        ccardr[i] = int(ccardr[i])
    
    for i in range(0, len(ccardr)):
        if ccardr[i] > 9:
            ccardr[i] = int(ccardr[i]) - 9

    validation = int(sum(ccardr) % 10)
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