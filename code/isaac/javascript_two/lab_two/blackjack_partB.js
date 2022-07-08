<<<<<<< Updated upstream
// Blackjack Advise

// Create an object of cards and their values
=======
// Blackjack Part B
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
// create input for player
let firstCard = document.querySelector('#card-one');
let secondCard = document.querySelector('#card-two');
let thirdCard = document.querySelector('#card-three');

let drawBtn = document.querySelector('#draw');
let div1 = document.querySelector('#div1');
=======
let drawBtn 

// create input for player
let firstCard = prompt("Draw your first card: ")
let secondCard = prompt("Draw your second card: ")
let thirdCard = prompt("Draw your third card: ")
>>>>>>> Stashed changes

// Create a function containing the players deck of cards
// return drawn cards and add all cards drawn

function cardDeck(cardOne, cardTwo, cardThree) {
<<<<<<< Updated upstream
    return playerDeck[cardOne.value] + playerDeck[cardTwo.value] + playerDeck[cardThree.value]
}
// console.log(cardDeck())
console.log(firstCard.value)


// sum up all cards drawn


drawBtn.addEventListener('click', function(){
    let cardsTotal = cardDeck(firstCard, secondCard, thirdCard) 
    console.log(cardsTotal)
    let finalDraw = cardsTotal

    if (finalDraw < lowestDraw) {
        div1.innerText = `Your cards are ${finalDraw} Hit`
    } else if (finalDraw >= lowestDraw && finalDraw < winningNumber) {
        div1.innerText = `Your cards are ${finalDraw} Stay`
    } else if (finalDraw > winningNumber) {
        div1.innerText = `Your cards are ${finalDraw} Bust`
    } else if (finalDraw === winningNumber) {
        div1.innerText = `Your cards are ${finalDraw} Blackjack!`
    }
})
=======
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
>>>>>>> Stashed changes
