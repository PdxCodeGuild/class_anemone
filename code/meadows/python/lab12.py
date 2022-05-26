import math
import random

class ATM:  # A newly created account will default to a '''balance of 0 and an interest rate of 0.1%'''. Implement the initializer
    def __init__(self,balance=0,interest=0.001):
        self.balance = balance
        self.interest = interest
        self.transaction = []
    def check_balance(self):
        return self.balance
    def calc_interest(self):
        return self.balance * self.interest
    def deposit(self, amount):
        self.balance += amount
        self.transaction.append(f'Deposit ${amount}')
    def check_withdrawal(self, amount):
        if (self.balance - amount) >= 0:
            return True
        else:
            return False
    def withdraw(self, amount):
        self.balance -= amount
        self.transaction.append(f'Withdrew ${amount}')
        return amount
    def transactions(self):
        return self.transaction

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
        transactions = atm.transactions()
        print(transactions)



    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - amount depoited/withdrew')
        print('exit     - exit the program')

    elif command == 'exit':
        break
    else:
        print('Command not recognized')

#work git push WORK!