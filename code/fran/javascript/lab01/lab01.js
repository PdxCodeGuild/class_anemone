// Lab01 - Blackjack Advice
// Fran Kappes

// Create object of card values

let card_values = {
    A: 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    J: 10,
    Q: 10,
    K: 10
}

// Collect card info from user
let card_1 = prompt("What's your first card? (2-9,A,K,Q,J)")
let card_2 = prompt("What's your second card? (2-9,A,K,Q,J)")
let card_3 = prompt("What's your third card? (2-9,A,K,Q,J)")

// Add card values and return advice on what to do next
// Assuming aces are always worth one point

// alert("card 1 value: " + card_values[card_1])   for testing
// alert("card 2 value: " + card_values[card_2])   for testing
// alert("card 3 value: " + card_values[card_3])   for testing

let hand_total = card_values[card_1] + card_values[card_2] + card_values[card_3]

// Return advice to user
if (hand_total < 17) {
    alert(hand_total + "...Hit")
} else if (hand_total >= 17 && hand_total < 21) {
    alert(hand_total + "...Stay")
} else if (hand_total === 21) {
    alert(hand_total + "...Blackjack!")
} else {
    alert('Already busted')
}
