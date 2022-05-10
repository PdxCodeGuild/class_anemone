' Lab 12 - ATM '

class ATM():

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        return round(self.balance, 2)

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"User deposited: ${amount}")

    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"User withdrew: ${amount}")

    def calc_interest(self):
        interest = self.balance * self.interest_rate
        return round(interest, 2)
    
    def print_transactions(self):
        print(f"Recent Transactions:\n {self.transactions}")
    
balance = 0
interest_rate = 0.001

atm = ATM(balance, interest_rate) # create an instance of our class
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
        amount = float(input('How much would you like? '))
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
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance      - get the current balance')
        print('deposit      - deposit money')
        print('withdraw     - withdraw money')
        print('interest     - accumulate interest')
        print('exit         - exit the program')
        print('transactions - view most recent transactions')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')