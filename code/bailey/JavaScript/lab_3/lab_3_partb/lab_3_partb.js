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
        this.transactions.push(' user deposited: ' + amount)
    }

    withdraw(amount){
        this.balance -= parseFloat(amount)
        this.transactions.push(' user withdrew: ' + amount)
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
let commandBtn = document.getElementById('command')
let resultsDiv = document.getElementById('results')
let depositDiv = document.getElementById('deposit')
let withdrawDiv = document.getElementById('withdraw')


console.log(atm.check_balance())

commandBtn.addEventListener('click', function(){
    let command = document.getElementById('commandText').value
    resultsDiv.replaceChildren()
    depositDiv.replaceChildren()
    if (command === 'balance'){
        balance = atm.check_balance()
        balance = balance.toFixed(2)
        let resultsP = document.createElement('h4')
        resultsP.innerText = `Your account balance is $${balance}`
        resultsDiv.replaceChildren(resultsP)
    }else if (command === 'deposit'){ 
        let depositP = document.createElement('input')
        depositP.setAttribute('id', 'depositText')
        depositP.setAttribute('type', 'text')
        let depositBtn = document.createElement('button')
        depositBtn.setAttribute('id', 'depositBtn')
        depositBtn.innerText = "Deposit"
        depositDiv.replaceChildren(depositP, depositBtn)
        let deposit = document.getElementById('depositBtn')

        deposit.addEventListener('click', function(){
            let amount = Number(document.getElementById('depositText').value)
            console.log(amount)
            atm.deposit(amount)
            depositDiv.replaceChildren(`Deposited $${amount}`)
        })
    }else if (command === 'withdraw'){
        let withdrawP = document.createElement('input')
        withdrawP.setAttribute('id', 'withdrawText')
        withdrawP.setAttribute('type', 'text')
        let withdrawBtn = document.createElement('button')
        withdrawBtn.setAttribute('id', 'withdrawBtn')
        withdrawBtn.innerText = "Withdraw"
        withdrawDiv.replaceChildren(withdrawP, withdrawBtn)
        let withdraw = document.getElementById('withdrawBtn')

        withdraw.addEventListener('click', function(){
            let amount = Number(document.getElementById('withdrawText').value)
            withdrawDiv.replaceChildren()
            if(atm.check_withdrawal(amount) == true){
                atm.withdraw(amount)
                let resultsP = document.createElement('h4')
                resultsP.innerText = `Withdrew $${amount}`
                resultsDiv.replaceChildren(resultsP)
            }
            else{
                let resultsP = document.createElement('h4')
                resultsP.innerText = "Insufficient funds! Check Balance and try again."
                resultsDiv.replaceChildren(resultsP)
            }
        })
    }else if(command === 'interest'){
        amount = atm.calc_interest()
        atm.deposit(amount)
        let resultsP = document.createElement('h4')
        resultsP.innerText = `Accumulated $${amount} in interest`
        resultsDiv.replaceChildren(resultsP)
    }else if(command === 'transactions'){
        transactions = atm.print_transaction()
        let resultsP = document.createElement('h4')
        resultsP.innerText = `List of transactions: ${transactions}`
        resultsDiv.replaceChildren(resultsP)
    }else{
        alert('command not recognized')
    }
})

