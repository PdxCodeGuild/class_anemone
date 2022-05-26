'''ATM'''

# Create an ATM class representing an ATM
class ATM:
    def __init__(self, balance=0, interest_rate=0.001):  # balance is 0 and interest rate is a 1% rate
        self.balance = balance
        self.interest_rate = interest_rate
        self.transaction = []
    
    def check_balance(self):  # this function is where you will check your balance
        return self.balance  # account balance will begin at zero(0).  return balance
    

    def deposit(self, amount):  # this function will deposit the amount the user has
        self.balance += amount
        self.transaction.append(f"You have deposited ${amount}")
    
    def check_withdrawl(self, amount):  # this function will return True if amount is not negative
        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):  # withdraw from the account and return amount
        self.balance -= amount
        self.transaction.append(f"You have withdrawn ${amount}")
        return amount
    
    def calc_interest(self):  # return calculated interest on the account
        return self.balance * self.interest_rate

    def print_transactions(self):  # print transaction history to the user
        print(self.transaction)
    
    # REPL of the ATM class

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
        if atm.check_withdrawl(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transaction':
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('transaction - view transactions')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')


        
        
    


