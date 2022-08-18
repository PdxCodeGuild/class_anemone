class ATM{
    constructor(balance = 0){
        this.balance = balance
        this.transactions = []
        this.interest = this.balance * 0.001
    }

    check_balance(){
        return this.balance
    }

    deposit(amount){
        this.balance += parseFloat(amount)
        this.transactions.push('user deposited: ' + amount)
    }

    withdraw(amount){
        this.balance -= parseFloat(amount)
        this.transactions.push('user withdrew: ' + amount)
    }

    check_withdrawal(amount){
        if (amount > this.balance){
            return false
        }else{
            return true
        }
    }

    calc_interest(){
        this.interest = this.balance * 0.001
        return this.interest
    }

    print_transaction(){
        return this.transactions
    }
}

let atm = new ATM()
let loop = true
console.log(atm.check_balance())

while(loop){
    command = prompt('Enter a command(Enter "help") for a list of the commands')
    const help = `Available commands:
    balance - get the current balance
    deposit - deposit money
    withdraw - withrdaw money
    interest - accumulate interest
    transactions - show account transactions
    exit - exit the program`

    if (command == 'balance'){
        balance = atm.check_balance()
        alert("Your balance is $" + balance)
    }else if (command == 'deposit'){
        amount = prompt('How much would you like to deposit?')
        atm.deposit(amount)
        alert("Deposited $" + amount)
    }else if (command == 'withdraw'){
        amount = prompt("How much would you like to withraw?")
        if(atm.check_withdrawal(amount) == true){
            atm.withdraw(amount)
            alert("Withdrew $" + amount)
        }
        else{
            alert('Insufficient funds')
        }
    }else if(command == 'interest'){
        amount = atm.calc_interest()
        atm.deposit(amount)
        alert("Accumulated $" + amount + " in interst")
    }else if(command == 'transactions'){
        transactions = atm.print_transaction()
        alert("List of transactions: " + transactions)
    }else if(command == 'help'){
        alert(help)
    }else if(command == 'exit'){
        loop = false
    }else{
        alert('command not recognized')
    }
}

