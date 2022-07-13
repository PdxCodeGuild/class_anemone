let card1 = prompt('What is your first card?')
let card2 = prompt('What is your second card?')
let card3 = prompt('What is your third card?')

let cardValues = {
    A : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10,
    J : 10,
    Q : 10,
    K : 10,
}

let total = cardValues[card1] + cardValues[card2] + cardValues[card3]

if (total < 17) {
    alert(total, "Hit")
} else if (total >= 17) {
    if (total > 21) {
        alert(total + "Already Busted")
    }
    if (total < 21) {
        alert(total + "Stay")
    }
    if (total === 21) {
        alert(total + "Blackjack!")
    }
}
