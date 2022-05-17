# Lab 12 V1 and V2

#corrections from first push, 
#   self.amount to amount
#   I had flipped some of the expressions in deposit and withdraw
#   need to make sure + is =+ and - is -=

class ATM:
    
    def __init__(self, balance=0, interest_rate=0.01):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def check_balance(self):
        return self.__balance
        
    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposit: ${amount}")

    def check_withdrawal(self, amount):
        return self.__balance >= amount
        #     return True
        # return False
        

    def withdraw(self, amount):
        self.__balance -= amount
        self.__transactions.append(f"Withdrawl: ${amount}")
        return amount


    def calc_interest(self):
        return self.__balance * self.__interest_rate

    def print_transactions(self):
        print("\n".join(self.__transactions))
        # return self.__transactions

    #private == __ BEST PRACTICE especially for an ATM when you do not want the user to be able to manipulate the variables


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
    elif command == 'record':
         atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('record   - print transaction history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
