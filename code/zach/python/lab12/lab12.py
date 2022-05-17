class ATM:
    def __init__(self, balance=0, interest_rate=0.001, transactions=[]):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = transactions

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        interest = self.balance * self.interest_rate
        return interest

    def print_transactions(self):
        return self.transactions


def main():
    atm = ATM()  # create an instance of our class
    print('Welcome to the ATM')
    while True:
        command = input('Enter a command: ')
        if command == 'balance':
            balance = atm.check_balance()  # call the check_balance() method
            print(f'Your balance is ${balance}')
        elif command == 'deposit':
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount)  # call the deposit(amount) method
            atm.transactions.append(f'user deposited ${amount}')
            print(f'Deposited ${amount}')
        elif command == 'withdraw':
            amount = float(input('How much would you like '))
            # call the check_withdrawal(amount) method
            if atm.check_withdrawal(amount):
                atm.withdraw(amount)  # call the withdraw(amount) method
                atm.transactions.append(f'user withdrew ${amount}')
                print(f'Withdrew ${amount}')
            else:
                print('Insufficient funds')
        elif command == 'interest':
            amount = atm.calc_interest()  # call the calc_interest() method
            atm.deposit(amount)
            print(f'Accumulated ${amount} in interest')
        elif command == 'transactions':
            transactions = atm.print_transactions()  # call the print_transactions() method
            print(f'Users Transactions: \n {transactions}')
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


if __name__ == '__main__':
    main()
