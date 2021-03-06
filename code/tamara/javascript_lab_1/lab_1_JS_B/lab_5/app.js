let submitBtn = document.getElementById('submit')


function ticket() {
    var ticketNumbers = []
    while (ticketNumbers.length < 7) {
        ticketNumbers.push(Math.floor(1 + Math.random()*99))
    }
    return ticketNumbers
}

submitBtn.addEventListener('click', function(){
    let num1 = parseInt(document.getElementById('num1').value)
    let num2 = parseInt(document.getElementById('num2').value)
    let num3 = parseInt(document.getElementById('num3').value)
    let num4 = parseInt(document.getElementById('num4').value)
    let num5 = parseInt(document.getElementById('num5').value)
    let num6 = parseInt(document.getElementById('num6').value)
    let num7 = parseInt(document.getElementById('num7').value)

    let balance = 0
    let winnings = 0
    let expenses = 0
    let winningTicket = []

    winningTicket.push(num1)
    winningTicket.push(num2)
    winningTicket.push(num3)
    winningTicket.push(num4)
    winningTicket.push(num5)
    winningTicket.push(num6)
    winningTicket.push(num7)

    totalTickets = 100000
    x = 0

    while (x < totalTickets) {
        let boughtTicket = ticket()
        let numberMatches = 0

        if (boughtTicket[0] === winningTicket[0]){
            numberMatches++
        }
        if (boughtTicket[1] === winningTicket[1]){
            numberMatches++
        }
        if (boughtTicket[2] === winningTicket[2]){
            numberMatches++
        }
        if (boughtTicket[3] === winningTicket[3]){
            numberMatches++
        }
        if (boughtTicket[4] === winningTicket[4]){
            numberMatches++
        }
        if (boughtTicket[5] === winningTicket[5]){
            numberMatches++
        }

        if (numberMatches === 1){
            balance += 4
            winnings += 4
        }
        if (numberMatches === 2){
            balance += 7
            winnings += 7
        }
        if (numberMatches === 3){
            balance += 100
            winnings += 100
        }
        if (numberMatches === 4){
            balance += 50000
            winnings += 50000
        }
        if (numberMatches === 5){
            balance += 1000000
            winnings += 1000000
        }
        if (numberMatches === 6){
            balance += 25000000
            winnings += 25000000
        }

        balance -= 2
        expenses += 2

        totalTickets--
    }

    let roi = balance/expenses

    let winning = document.getElementById('winning-ticket')
    let winningP = document.createElement('p')
    winningP.innerText = `The winning ticket number is ${winningTicket}`
    winning.insertBefore(winningP, winning.firstChild)

    let results = document.getElementById('results')
    let resultsP = document.createElement('p')
    resultsP.innerText = `Your balance is $${balance} your winnings are $${winnings} and your expenses were $${expenses}. Your ROI is ${roi}`
    results.insertBefore(resultsP, results.firstChild)

})