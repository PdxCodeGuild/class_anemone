// Lab02 *** Part B - Pick 6
// Fran Kappes


//  Define pick6 function, that randomly generates 6 numbers
//  This will be used to generate the winning numbers and the 100,000 lottery tickets
function pick6() {
    // console.log("Inside pick6 function")    //TEST

    let ticket = []

    let i = 0

    while (i < 6) {
        let number = (Math.floor(1 + Math.random()*98)) // random integer 1-99
        ticket.push(number)
        i++
    }

    // console.log("pick6 function ticket: " + ticket)  //TEST

    return ticket
}


// Define num_matches function, which determines the number of matches
// between the winning numbers and a lottery ticket
function numMatches(lottery_ticket, winning_ticket) {
    // console.log("Inside numMatches function")   //TEST

    let i = 0
    let matches = 0

    // Compare the lottery ticket numbers to the winning ticket numbers
    // To be a match, numbers in the same position for both tickets must match 
    while (i < 6) {
        if (lottery_ticket[i] === winning_ticket[i]) {
            matches++
        }

        i++
    }

    return matches    
}


// Define payout function. This function determines the lottery ticket holder's
// payout based on the number of matches to the winning ticket
function getPayout(matches) {
    // console.log("Inside getPayout function")    //TEST

    let payout_scale = {
        '0': 0,
        '1': 4,
        '2': 7,
        '3': 100,
        '4': 50000,
        '5': 1000000,
        '6': 25000000
    }

    let payout = payout_scale[matches]

    return payout
}

let calculateBtn = document.getElementById('calculate')
let resultsDiv = document.getElementById('results')

calculateBtn.addEventListener('click', function() {
    // Define and initialize balance variable
    balance = 0

    // Generate the winning ticket. This will be a list of numbers.
    let winning_ticket = pick6()
    // console.log("winning_ticket: " + winning_ticket)  //TEST 


    // Main loop. This loop will run 100,000 times. Each loop will do a number of things:
    //     Generate a lottery ticket and compare the winning numbers to the lottery ticket.
    //     Subtract 2 from the balance (you bought a $2 lottery ticket)
    //     Find out how many numbers match
    //     Add to your balance the winnings from your matches

    total_winning_payout =  0   
    total_num_wins = 0   

    i = 0

    while (i < 100000) {

        // console.log("balance before subtracting $2: " + balance)  //TEST

        // pay $2 for a ticket
        balance -= 2  
        
        // get lottery ticket
        lottery_ticket = pick6()  
        // console.log("lottery ticket: " + lottery_ticket)  //TEST

        // find out if any numbers match
        matches = numMatches(lottery_ticket, winning_ticket)
        // console.log("matches: " + matches)          //TEST

        // find out winning payout, if any, for this ticket
        payout_amount = getPayout(matches)
        // console.log("payout_amount: " + payout_amount)   //TEST

        if (payout_amount > 0) {
            total_winning_payout += payout_amount
            total_num_wins += 1        
            
            // console.log("payout_amount: " + payout_amount)      //TEST
            // console.log("total_winning_payout: " + total_winning_payout)      //TEST
        }

        // add winnings payout to balance
        balance += payout_amount
        // console.log("balance at end of this loop: " + balance)  //TEST

        // increment loop counter
        i++
    }


    // Calculate ROI (return on investment)
    // Note: total expenses = 100,000 tickets * $2 per ticket = 200,000
    // Because number of tickets is hard-coded, I'm hard-coding the total expenses
    let roi = (total_winning_payout - 200000)/200000


    // format final balance and total winning payout
    balance = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
    }).format(balance)

    total_winning_payout = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
    }).format(total_winning_payout)

    let resultP = document.createElement('p')
    resultP.innerText = `
        Final balance: ${balance}
        Total earnings: ${total_winning_payout}
        Total expenses: $200,000
        ROI: ${roi}
        Total number of wins: ${total_num_wins}
    `
    resultsDiv.prepend(resultP)
})