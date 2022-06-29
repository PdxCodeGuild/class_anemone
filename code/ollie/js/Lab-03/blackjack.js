let cards = {
    'A': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10
}

let first_card = cards[prompt("What is your first card?")]
let second_card = cards[prompt("What is your seocnd card?")]
let third_card = cards[prompt("What is your third card?")]

function advice(card1, card2, card3) {
    if ((card1 + card2 + card3) < 17) {
        alert(`${card1 + card2 + card3}, Hit.`)
    } else if ((card1 + card2 + card3) >= 17 && (card1 + card2 + card3) < 21) {
        alert(`${card1 + card2 + card3}, Stay...`)
    } else if ((card1 + card2 + card3) === 21) {
        alert(`${card1 + card2 + card3}, Blackjack!`)
    } else if ((card1 + card2 + card3) > 21) {
        alert(`${card1 + card2 + card3}, Busted.`)
    }
}
advice(first_card, second_card, third_card)