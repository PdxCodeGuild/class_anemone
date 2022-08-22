

var cards = {
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


var first_card = prompt("What is your first card: ")

var second_card = prompt("What is your second card: ")

var third_card = prompt("What is your third card: ")

var points = cards[first_card] + cards[second_card] + cards[third_card]


if (points >= 17 && points < 21) {
    alert(points + ! "You should stay here!")
}
if (points == 21){
    alert(points + "Blackjack")
}

if (points > 21){
    alert(points + "Busted! You lost..")
}

if (points < 17){
    alert(points + "Hit")
}