let card1 = prompt("Enter your first card: ").toUpperCase()
let card2 = prompt("Enter your second card: ").toUpperCase()
let card3 = prompt("Enter your third card: ").toUpperCase()
console.log(card1)
console.log(card2)
console.log(card3)

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

console.log(card1)
console.log(card2)
console.log(card3)

// alert('Your card is ' + card1 + card2 + card3);

let hand = parseInt(card1) + parseInt(card2) + parseInt(card3)

if (hand > 1 && hand < 17) {
    alert('Your hand is ' + hand + ' I would HIT')
}
else if (hand >= 17 && hand < 21 ) {
    alert('Your hand is ' + hand + ' I would Stay')
}
else if (hand === 21) {
    alert('Your hand is ' + hand + ' BLACK JACK BABY!!!!')
}
else {
    alert('Your hand is ' + hand + ' YOU BUSTED!')
}
// alert ('Your hand is ' + hand)