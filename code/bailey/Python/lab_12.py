'''
Class Anemone
Lab 12
Bailey Baker
'''


class ATM:
    def __init__(self):
        self.balance = 0     # Initiate users balance
        self.transactions = []   # initiate transaction list

    def check_balance(self):    # funciton to return class balance
        return round(self.balance, 2)

    def deposit(self, amount):
        self.balance += amount   # function to 'deposit' to account, adds to balance
        self.transactions.append(f'user deposited: {amount}')

    def withdraw(self, amount): # function to 'withdraw' from account, dubtracts from balance
        self.balance -= amount
        self.transactions.append(f'user withdrew: {amount}')

    def check_withdrawal(self, amount): # function to check if account has enough to conduct withdrawal
        if amount > self.balance:
            return False
        else:
            return True

    def calc_interest(self):  # function to calculate interest of total balance and return interest amount
        interest = self.balance * 0.001 
        return round(interest, 2)

    def print_transaction(self): # function to return transactions to be printed
        return self.transactions

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
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
        transactions = atm.print_transaction()  # call the print_transaction() method
        print(f'List of transactions: {transactions}')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - show account transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')