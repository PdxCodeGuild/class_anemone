let firstcard = prompt('What is your first card?:  ')
let secondcard = prompt('What is your second card?:  ')
let thirdcard = prompt('What is your third card?:  ')

let cards = {
    'A':1,
    'J':10,
    'K':10,
    'Q':10,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10
    }
    
let fc = cards[firstcard]
let sc = cards[secondcard]
let tc = cards[thirdcard]

let hand = fc+sc+tc

alert(hand)

if (hand == 21){
    alert('Blackjack')}
else if (hand >= 21){
    alert('Already busted')}
else if (hand <17){
    alert('Hit')}
else if (hand >= 17 && hand < 21){
    alert('Stay')}

