import random
trans_id=[]
def trans_id_assign(trans_id):
    while len(trans_id) < 6:
        trans_id.append(random.randint(1,9))
    return trans_id

balance = 0
rate = .1
trans_t = [{"action":"withdraw", "amount": 0, "begin balance":0, "end balance": 0}]
transactions = []

class ATM:
    def __init__(self, balance, rate):
        self.transactions = transactions
        self.balance = balance
        self.rate = rate
        # print(balance)

    def check_balance(self):
        return self.balance 
        

    def deposit(self, amount):
        self.balance += amount


    def withdrawal_attempt(self, amount):
        self.amount = amount
        if amount <= self.balance:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        
    def calc_interest(self, rate):
        interest = self.balance * rate    
        return interest

    


    def print_transactions(self, transactions):
        trans_id=trans_id_assign(trans_id)
        print(trans_id, transactions)
        return transactions

    
    
# balance = ATM(1000,.05)



atm = ATM(balance, rate) # create an instance of our class
# print(type(atm))
print('Welcome to the ATM')
while True:
    # trans_id = random.randint()
    command = input("""\n\tSelect option:
    \t(b) Balance Inquiry
    \t(d) Make a Deposit
    \t(w) Make a Withdrawal
    \t(i) View Interest Accumulation
    \t(t) Transaction Records
\nenter 'exit' to quit...\n""")
    if command == 'balance' or command == 'b':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit' or command == 'd':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}, New balance: ${atm.check_balance()}')
        x = f"trans #{trans_id} : {command}, amount: {amount}, ending balance: {atm.check_balance()}"
    elif command == 'withdraw' or command == 'w':
        amount = float(input('How much would you like '))
        if atm.withdrawal_attempt(amount): # call the check_withdrawal(amount) method
            balance = atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}; balance: ${atm.check_balance()}')

            x = f"trans #{trans_id}: {command}, amount: {amount}, ending balance: {atm.check_balance()}"
        else:
            print('Insufficient funds')
    elif command == 'interest' or command == 'i':
        amount = atm.calc_interest(rate) # call the calc_interest() method    
        print(f'${amount} in interest will accumulate over the next 12 months at current balance of ${atm.check_balance()}')
    elif command == 'transactions' or command == 't':
        print("Transaction Report Summary: ")
        transactions = (atm.print_transactions(transactions))  
        trans_id = transactions.pop()
        print(transactions)  
    # elif command == 'help':
    #     print('Available commands:')
    #     print('balance  - get the current balance')
    #     print('deposit  - deposit money')
    #     print('withdraw - withdraw money')
    #     print('interest - accumulate interest')
    #     print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

print(f"final balance: {atm.check_balance()}")    
