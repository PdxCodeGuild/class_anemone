class ATM():
    balance = 0
    account_changes = []
    
    
    def __init__(self):
        pass 
    

    def check_balance(self):
        balance = ATM.balance
        ATM.account_changes.append('User checked balance.')
        return balance
    

    def check_withdrawal(self, amount):
        if ATM.balance - amount < 0:
            ATM.account_changes.append('User had insufficent funds.')
            return 
        elif ATM.balance - amount > 0:
            return True
    
    
    def withdraw(self, amount):
        if ATM.check_withdrawal(self, amount) == None:
            return
        elif ATM.balance - amount > 0:
            ATM.account_changes.append(f'User withdrew {amount}.')
            ATM.balance -= amount
            return ATM.balance
    
    
    def deposit(self, amount):
        ATM.account_changes.append(f'User deposited {amount}.')
        ATM.balance += amount
        return ATM.balance
    
    
    def calc_interest(self):
        interest = ATM.balance * .0001
        ATM.balance += interest
        ATM.account_changes.append(f'User acummilated {interest}.')
        return interest
    

    def transactions(self):
        transactions = '\n'.join(ATM.account_changes)
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
    elif command == 'transactions':
        inter = atm.transactions()
        print(inter)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('transactions - returns a list of account trasactions')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')