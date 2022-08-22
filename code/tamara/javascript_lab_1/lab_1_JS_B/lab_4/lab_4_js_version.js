let submitBtn = document.getElementById('submit')

submitBtn.addEventListener('click', function () {

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

    let firstCard = document.getElementById('first-card')
    let secondCard = document.getElementById('second-card')
    let thirdCard = document.getElementById('third-card')
    let results = document.getElementById('results')

    let firstCardValue = cardValue[firstCard.value]
    let secondCardValue = cardValue[secondCard.value]
    let thirdCardValue = cardValue[thirdCard.value]

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

    let resultsP = document.createElement('p')
    resultsP.innerText = `${totalCardValue} ${advice}`
    results.insertBefore(resultsP, results.firstChild)
})



