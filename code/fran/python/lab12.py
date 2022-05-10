# Lab12 - ATM
# Fran Kappes

class ATM():
    # Define initialization method
    def __init__(self): 
        self.balance = 0
        self.interest_rate = 0.001
        # self.transaction_history = []

    # Define check balance method
    def check_balance(self):
        
        # Fetch balance and return to user
        return self.balance


    # Define deposit method
    def deposit(self, deposit_amount):
        self.balance += deposit_amount


    # # Define check withdrawl amount method, which checks balance prior to withdrawal attempt
    def check_withdrawal(self, withdrawal_amount):
        if withdrawal_amount <= self.balance:
            return True
        elif withdrawal_amount > self.balance:
            return False


    # # Define withdraw method
    def withdraw(self, withdrawal_amount):
        self.balance -= withdrawal_amount


    # # Define calculate interest method
    def calc_interest(self):
        interest = self.balance * self.interest_rate

        return interest


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