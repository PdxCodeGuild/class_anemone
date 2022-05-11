class ATM:
    def __init__(self, balance=0, interest_rate=.001):
        self.__balance = balance # these should be private varibles now
        self.__interest_rate = interest_rate
        self.__transactions_list = []

    def print_transactions(self):
        return self.__transactions_list

    def check_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount 
        self.__transactions_list.append(f"User deposited {amount}$")
        return self.__balance
    
    def check_withdrawal(self, amount):
        return amount <= self.__balance
    
    def withdraw(self, amount):
        self.__balance -= amount
        self.__transactions_list.append(f"User withdrew {amount}$")
        return amount
    
    def calc_interest(self): 
        interest_made = self.__interest_rate * self.__balance
        self.__transactions_list.append(f"User made {interest_made}$ in interest")
        return interest_made
    

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
        transactions = atm.print_transactions()
        transactions = '\n'.join(transactions)
        print(transactions)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get a list of transactions conducted')
        print('exit - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')