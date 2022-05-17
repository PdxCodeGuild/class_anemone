class ATM:
    def __init__(self):
        self.balance = 0
        self.interest = 0.01
        self.transactions = []

    def check_balance(self):
        # check the balance for account
        balance = self.balance
        return balance

    # check the amount for deposit
    def deposit(self, amount):
        self.transactions.append(f"Deposited: {amount}")
        if amount > 0:
            self.balance += amount
            # print(f"\n Remaining balance is: ${self.balance}")
            return amount

    # check the amount for withdrawal
    def check_withdrawal(self, amount):
        self.transactions.append(f"Withdrawal: {amount}")
        # print(f"\n Remaining balance is: ${self.balance}")
        return self.balance > amount

    # check amount vs balance
    def withdraw(self, amount):
        self.balance -= amount
        return amount

    # check the amount of interest for account
    def calc_interest(self):
        amount = self.balance * self.interest
        return amount

    # show recorded transaction
    def transaction(self):
        for i in range(len(self.transactions)):
            print(self.transactions[i])
        # print(f"\n Remaining balance is: ${self.balance}")


atm = ATM()  # create an instance of our class
print("Welcome to the ATM")

menu = {
    "1": "Balance",
    "2": "Deposit",
    "3": "Withdraw",
    "4": "Interest",
    "5": "Print Transactions",
    "6": "Exit", }

while True:
    print()
    for label, option in menu.items():
        print(f"{label}, {option}")
    command = input("Please make your selection below: ").lower()
    command = menu.get(command)

    if command == "Balance":
        balance = atm.check_balance()
        print(f"Your current balance is: ${balance}")

    elif command == "Deposit":
        amount = float(input(f"How much would you like to deposit: "))
        check = atm.deposit(amount)  # call the deposit(amount) method
        print(f"Deposited: ${amount}")

    elif command == "Withdraw":
        amount = float(input("How much would you like: "))
        if atm.check_withdrawal(amount):  # call the check_withdrawal(amount) method
            check = atm.withdraw(amount)  # call the withdrawal(amount) method
            print(f"Withdrew: ${amount}.\nRemaining balance is: {atm.check_balance()}")
        else:
            print("Insufficient funds. ")

    elif command == "Interest":
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f"Accumulated ${round(amount, 2)} in interest. ")

    elif command == "Print Transactions":
        atm.transaction()

    elif command == "Exit":
        print("Have a nice day!")
        break
    else:
        print("Command not recognized. ")
