class ATM():
      
    

    def __init__(self, balance = 0, interest = 0.001):
        self.balance = balance
        self.interest = interest
        self.changes =  []
        pass 
    

    def check_balance(self):
        self.changes.append('User checked balance.')     # appends the list with the account interaction
        return self.balance                                     # return ATM self.balance
    

    def check_withdrawal(self, amount):
        if self.balance < amount:                            # checks whether user has sufficent funds
            self.changes.append('User had insufficent funds.')   # appends the list with the account interaction
            return 
        elif self.balance > amount:                          # returns True if balance is greater than requested amount
            return True
    
    
    def withdraw(self, amount):
        if self.check_withdrawal(amount) == None:              # pulls in None or True form check withdrawl
            return                                                  # returns None if inported None
        elif self.check_withdrawal(amount) == True:
            self.changes.append(f'User withdrew {amount}.')  # appends the list with the account interaction
            self.balance -= amount                                   # modifys the ATM balance with the amount withdrawn
            return self.balance
    
    
    def deposit(self, amount):
        self.changes.append(f'User deposited {amount}.')     # appends the list with the account interaction
        self.balance += amount                                       # modifys the ATM balance with the amount deposited
        return self.balance
    
    
    def calc_interest(self):
        accum = self.balance * self.interest
        # ATM.balance += interest  and now i understand the deposit in the loop # modifys the ATM balance with the amount of interest earned
        self.changes.append(f'User acummilated {accum} in interest.') # appends the list with the account interaction
        return accum
    

    def transactions(self):
        self.changes.append(f'User requested list of account transactions.') # appends the list with the account interaction
        transactions = '\n'.join(self.changes)                               # splits the list into new lines for easier reading
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