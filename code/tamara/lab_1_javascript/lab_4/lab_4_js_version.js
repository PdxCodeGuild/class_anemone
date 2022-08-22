let cardValue = {
    'A': 1, 
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    '10' : 10, 
    'J': 10, 
    'Q': 10, 
    'K': 10
    }

function blackjackCounting(firstCard, secondCard, thirdCard) {
    let firstCardValue = cardValue[firstCard]
    let secondCardValue = cardValue[secondCard]
    let thirdCardValue = cardValue[thirdCard]

    var totalCardValue = parseInt(firstCardValue + secondCardValue + thirdCardValue)

    if (totalCardValue < 17) {
        var advice = 'hit'
    }
    else if (totalCardValue < 21 && totalCardValue > 16) {
        var advice = 'stay'
    }
    else if (totalCardValue === 21) {
        var advice = 'Blackjack'
    }
    else {
        advice = 'already busted'
    }
    return alert(`${totalCardValue} ${advice}`)
}

alert("Your card options are A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K")

let firstCard = prompt("What's your first card? ")
let secondCard = prompt("What's your second card? ")
let thirdCard = prompt("What's your third card? ")

blackjackCounting(firstCard, secondCard, thirdCard)