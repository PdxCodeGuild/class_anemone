// Disclaimer: Blackjack is typically played with


let cards = { // object for referencing card count
    'A':11,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,
}
let handCt=0 // tracks users hand count
cardKey = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] // list to reference card values 
//          0   1   2   3   4   5   6   7   8   9   10  11  12
// object for card value
i = 1 // counter for 'ordinal' card
let advice // declared for while loop
let hand = [] // declared for while loop to store player's hand
let cont // declared for continuing during game
let busted  //declared for determining ending message 
function msg(hand, handCt, advice) { // template literal depending on hand
    if (handCt < 17) {
        advice = 'hit..'
    } else if (handCt >= 17 && handCt <= 20) {
        advice = 'stay..'
    } else if (handCt === 21) {
        advice = 'BlackJack!'
    } else {
        advice = 'BUSTED'
    }
    return `hand: ${hand} \ncount: ${handCt}\nAdvice: ${advice}`
}
function cardDisplay (card) { // template literal for each card dealt
    return `card dealt: ${card}`
}
alert('Place your bets! ')  // beginning game message 
while (handCt <= 21) {

    if (handCt >= 21) {
        break
    } else {
        let cardIndex = Math.floor(Math.random()*cardKey.length) // random index of above array
        console.log('card', i, '(index): ', cardIndex) //print 1st card index
        let card = cardKey[cardIndex] // declare the first card
        hand.push(card)
        console.log('card',i,'(name):', card) // print 1st card
        cardKey.splice(cardIndex,1) // get rid of used card 
        console.log(cardKey) // print to check to make sure it's gone
        console.log(hand) // print current hand
        i++ // add 1 to number i am using above to indicate which 'ordinal' card 
        if (handCt <= 20 && card === 'A') {
            handCt++
        } else {
            handCt += cards[card]        
        }
        console.log(handCt)
        
        alert(cardDisplay(card)) 
        message = msg(hand, handCt, advice)
        alert(message)
        if (handCt <= 21) {
            cont = prompt("Hit? 'y' or 'n' : ")
            while (cont !== 'y' && cont !== 'n' && handCt != 21) {
                if (cont === 'y') {
                    continue 
                } else if (cont === 'n') {
                    break
                }
            }
            
        } else {
            busted = true
            break
        }
        if (cont === 'n') {
            break
        }
    }
    }
message = msg(hand, handCt)
alert(message)
if (busted === true) {
    alert('you busted!')
} else if (handCt >= 18 && handCt <= 20) {
    alert('great hand!')
} else if (handCt === 21) {
    alert('excellent hand!')
} else {
    alert('Wow, what a gamble...')
}

    
    

