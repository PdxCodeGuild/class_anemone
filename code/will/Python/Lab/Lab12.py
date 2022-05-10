import math
from typing import final

'''
atm.check.balance()
atm.deposit(amount)
atm.check_withdrawal()
atm.withdraw(amount)
atm.calc_interest()
atm.deposit(amount)
'''
#Establishing the class

class ATM:


#Writing functions for each function referenced in the REPL
    def __init__(Self, balance,):
        Self.balance = balance
        Self.interest = 0.01
        
    

    def check_balance(Self):
        return Self.balance
        


    def deposit(Self, amount):
        Self.balance += amount
        print (f' User added {amount} to their account. your account balance is {Self.balance}')

    def check_withdrawal(Self, amount):
        if amount <= Self.balance:
            return True
        elif amount > Self.balance :
            print ('Insufficent Funds ')

    def withdraw(Self, amount):
        Self.balance -= amount
        print(f' You withdrew {amount} - Your remaining balance is {Self.balance}')

    def calc_interest(Self):
        interest = []
        Self.interest = 0.01
        Self.calc_interest = (Self.balance * Self.interest)
        print(f' Accoutn interest equals {Self.calc_interest}')
        int(Self.calc_interest)
        return Self.calc_interest

        

        


            







atm = ATM(0) 


print('Welcome to the ATM')
while True:
    command = input('Enter a command: - (deposit, balance, withdraw, interest, help, exit: )')
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
        #atm.deposit(amount)
        print(f'Accumulated ${atm.calc_interest} in interest')
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