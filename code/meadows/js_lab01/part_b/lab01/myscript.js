let card1 = document.getElementById('card1')
let card2 = document.getElementById('card2')
let card3 = document.getElementById('card3')
let resultsDiv = document.getElementById('results')
let Hit =document.getElementById('hit')

//card 1
if (card1 === 'A') {
    card1 = 1
}
else if(card1 > 1 && card1 < 10) {
    card1 === card1
}
else if ( card1 === 'Q'|| card1 === 'J'|| card1 === 'K') {
    card1 = 10
}


// card 2
if (card2 === 'A') {
    card2 = 1
}
else if(card2 > 1 && card2 < 10) {
    card2 === card2
}
else if ( card2 === 'Q'|| card2 === 'J'|| card2 === 'K') {
    card2 = 10
}


//card 3
if (card3 === 'A') {
    card3 = 1
}
else if(card3 > 1 && card3 < 10) {
    card3 === card3
}
else if ( card3 === 'Q'|| card3 === 'J'|| card3 === 'K') {
    card3 = 10
}

Hit.addEventListener('click', function() {
    let answer = parseInt(car1.value) + parseInt(card2.value) + parseInt(card3.value)
    let blackjack = document.createElement('bj')
    blackjack.innerText = answer
    resultsDiv.insertBefore(blackjack, resultsDiv.firstChild)

})