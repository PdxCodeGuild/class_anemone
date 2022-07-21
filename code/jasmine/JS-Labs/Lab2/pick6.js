winning_nums = []
pick6(winning_nums)

let earnings = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000

}

function randint(a, b) {
    return Math.floor(a + Math.random()*b)
}

function pick6(arr) {
    while (arr.length < 6)
        arr.push(randint(1,99))
    return arr
}

function num_matches (win, ticket) {
    let matches=0
    for (let i=0; i<win.length; i++) {        
        if (win[i] === ticket[i]) {
            matches += 1
        }
    } return matches
}


let btn = document.querySelector("#btn")
btn.addEventListener("click", function () {
    let new_balance = document.querySelector("#new_balance")
    let balance = 0
    let counter = 0 
    let ticket
    let act_earnings =0
    let expenses =0
    let rounds = document.querySelector("#rounds")


    while (counter<rounds.value) {
        ticket = []
        counter ++
        balance -= 2 
        matches = 0
        expenses += 2

        pick6(ticket)
        balance += earnings[num_matches(winning_nums, ticket)]
        act_earnings += earnings[num_matches(winning_nums, ticket)]

    }

    let roi = (act_earnings-expenses)/expenses
    new_balance.innerText = `Expenses: $${expenses}\nWinnings: $${act_earnings}\nBalance: $${balance}\nROI: $${roi}`

})