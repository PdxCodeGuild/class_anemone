class ATM():
    balance = 0                                                 # set a base balance in the ATM class and a list to be appended with changes    
    account_changes = []
    
    
    def __init__(self):
        pass 
    

    def check_balance(self):
        balance = ATM.balance                                   # checks what the ATM balance is showing and inports it to the def to be returned
        ATM.account_changes.append('User checked balance.')     # appends the list with the account interaction
        return balance
    

    def check_withdrawal(self, amount):
        if ATM.balance - amount < 0:                            # checks whether user has sufficent funds
            ATM.account_changes.append('User had insufficent funds.')   # appends the list with the account interaction
            return 
        elif ATM.balance - amount > 0:                          # returns True if so to be passed into withdraw function
            return True
    
    
    def withdraw(self, amount):
        if ATM.check_withdrawal(self, amount) == None:              # pulls in None or True form check withdrawl
            return                                                  # returns None if inported None
        elif ATM.balance - amount > 0:
            ATM.account_changes.append(f'User withdrew {amount}.')  # appends the list with the account interaction
            ATM.balance -= amount                                   # modifys the ATM balance with the amount withdrawn
            return ATM.balance
    
    
    def deposit(self, amount):
        ATM.account_changes.append(f'User deposited {amount}.')     # appends the list with the account interaction
        ATM.balance += amount                                       # modifys the ATM balance with the amount deposited
        return ATM.balance
    
    
    def calc_interest(self):
        interest = ATM.balance * .0001                              # calculates interest earned of .01%
        # ATM.balance += interest  and now i understand the deposit in the loop # modifys the ATM balance with the amount of interest earned
        ATM.account_changes.append(f'User acummilated {interest}.') # appends the list with the account interaction
        return interest
    

    def transactions(self):
        ATM.account_changes.append(f'User requested list of account transactions.') # appends the list with the account interaction
        transactions = '\n'.join(ATM.account_changes)                               # splits the list into new lines for easier reading
        return transactions







atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ').lower()
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':                                         # added transactions elif for user to check account transactions
        inter = atm.transactions()
        print(inter)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('transactions - returns a list of account trasactions')                  # add transactions for user
    elif command == 'exit':
        break
    else:
        print('Command not recognized')