// Blackjack Advise

// Create an object of cards and their values

let playerDeck = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

// winning number. Player should try for >= 17 or <= 21
// Winning number is 21
let winningNumber = 21
let lowestDraw = 17

// create input for player
let firstCard = prompt("Draw your first card: ")
let secondCard = prompt("Draw your second card: ")
let thirdCard = prompt("Draw your third card: ")

// Create a function containing the players deck of cards
// return drawn cards and add all cards drawn

function cardDeck(cardOne, cardTwo, cardThree) {
    return playerDeck[cardOne] + playerDeck[cardTwo] + playerDeck[cardThree]
}
// console.log(cardDeck(firstCard, secondCard, thirdCard))

// sum up all cards drawn

let cardsTotal = cardDeck(firstCard, secondCard, thirdCard) 

if (cardsTotal in playerDeck) {
    alert(cardsTotal)
}

// compare cards drawn and display hit, stay, blackjack or bust.

if (cardsTotal < lowestDraw) {
    alert(`${cardsTotal} Hit`)
} else if (cardsTotal >= lowestDraw && cardsTotal < winningNumber) {
    alert(`${cardsTotal} Stay`)
} else if (cardsTotal > winningNumber) {
    alert(`${cardsTotal} Busted!!`)
} else if (cardsTotal === winningNumber) {
    alert(`${cardsTotal} Blackjack!`)
}