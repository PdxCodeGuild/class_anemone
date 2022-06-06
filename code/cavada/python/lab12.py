import random # imported to generate random numbers for transaction ids
# trans_id=[] 
def trans_id_assign():
    trans_id = []
    while len(trans_id) < 6:
        trans_id.append(str(random.randint(1,9)))
    t_id = ''
    for t in trans_id:
        t_id+=t
    return t_id      

balance = 0 # set account balance to zero
rate = .1 # 10% interest rate for interest accumulation function
# trans_template = [{"action":"transaction", "amount": 0, "begin balance":0, "end balance": 0}]

class ATM: # class set to contain all the functions relevant to the instantion represened by calling the balance and rate through it to essentially simulate an ATM session
    def __init__(self, balance=0, rate=.001): #dunder init function set to store running variables for rate, balance, and transactions
        self.transactions = [] # creates shell for storing transactions
        self.balance = balance # sets this as class varible
        self.rate = rate # set this as class variavle

    def trans_id_assign():
        trans_id = []
        while len(trans_id) < 6:
            trans_id.append(str(random.randint(1,9)))
            t_id = ''
            for t in trans_id:
                t_id+=t
                return t_id      

    def check_balance(self): # function to access the current state of the class variable balance
        return self.balance 
        
    def deposit(self, amount): # function to make a 'deposit'; essentially add a value to balance value corresponding to the deposit amount
        self.balance += amount
        trans_id = trans_id_assign()
        self.transactions.append(f"trans #{trans_id}: \n\tdeposit, amount: ${amount}, ending balance: ${self.balance}") # saves transaction info

    def withdrawal_attempt(self, amount): # function to check if withdraw can be made if the withdrawal won't exeed available funds, or bring balance below zero
        self.amount = amount
        if amount <= self.balance:
            return True

    def withdraw(self, amount): # function to reduce balance by value amount 
        self.balance -= amount
        trans_id = trans_id_assign() # uses function to get a random transaction id number (hash method)
        self.transactions.append(f"trans #{trans_id}: \n\twithdraw, amount: ${amount}, ending balance: ${self.balance}")
        
    def calc_interest(self): # tells user the amount of interest expected after 12 accumulation
        interest = self.balance * self.rate
        self.balance += interest    
        return interest

    def print_transactions(self): # funtction to bring transaction list to global 
        return self.transactions

atm = ATM() # create an instance of our class, 

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
        
    elif command == 'withdraw' or command == 'w':
        amount = float(input('How much would you like '))
        if atm.withdrawal_attempt(amount): # call the check_withdrawal(amount) method
            balance = atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}; balance: ${atm.check_balance()}')
        else:
            print('Insufficient funds')
            
    elif command == 'interest' or command == 'i':
        current = atm.balance
        atm.calc_interest() # call the calc_interest() method 
        new = round(atm.balance,2) 
        diff = round(new-current,2)
        print(f"new balance: ${new}\nold balance: ${current}\ninterest({(atm.rate)*100}%): ${diff}")  

    elif command == 'transactions' or command == 't':
        print("Transaction Report Summary: ")
        transactions = atm.print_transactions()
        for trans in transactions:
            print(trans)

    elif command == 'exit': # exit instance of atm
        break

    else:
        print('Command not recognized')

print("account activity summary: ")

print(f"final balance: ${atm.check_balance()}") # print of final balance
for trans in transactions: 
    print(trans) # print each transaction from list compiled during instantiation of ATM class


