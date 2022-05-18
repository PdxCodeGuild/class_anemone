

##ATM Lab12
from decimal import Decimal

## Class object for ATM / Parent Class
class ATM:
    ##init funtion to initialize the account object
    def __init__(self):
        # self.name = name
        self.balance = 0
        self.interest_rate = 0.001
        self.transactions = []
        #if balance is less than 0, raise an exception
        # if balance < Decimal('0.00'):
        #     raise ValueError('Initial Balance must be >= to 0.00.')

    ## check current balance
    def check_balance(self):
        return self.balance

    ## deposit methos to add positive amt to acct
    def deposit(self, amount):
        # if amount < Decimal('0.00'):
        #     raise ValueError('amount must be positive.')
        # self.amount = amount
        #if the deposit amount is valid. add to obj balance
        self.balance += amount
        self.transactions.append(f'Amount deposited ${amount}')

    ## withdraw money from the acct balance
    def withdraw(self,amount):
        #if amount is greater than avail balance raise exception
        # if amount > self.balance:
        #     raise ValueError('amount must be <= to balance.')
        # elif amount < Decimal('0.00'):
        #     raise ValueError('amount must be postive.')
        
        #if withdraw amount is valid
        self.balance -= amount
        self.transactions.append(f'Amount withdrawn ${amount}')

    ## check withdrawal amount
    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            return True

    # ## returns amount of interest 
    def calc_interest(self):
        return self.balance * self.interest_rate

    ## show transactions
    def show_transactions(self):
        return self.transactions

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')

    elif command == "transaction":
        transaction = atm.show_transactions()
        print(f'{transaction}')
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
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

    