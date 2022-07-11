let card1 = document.getElementById('card1')
let card2 = document.getElementById('card2')
let card3 = document.getElementById('card3')
let adv = document.getElementById('advice')
let suggest = document.getElementById('suggestion')
let output

adv.addEventListener('click', function() {
    let sum = 0
    sum += parseFloat(card1.value) + parseFloat(card2.value) + parseFloat(card3.value)
    if (sum < 17) {
        output = 'Hit.'
    } else if (sum >= 17 && sum < 21) {
        output = 'Stay.'
    } else if (sum === 21) {
        output = 'Blackjack!'
    } else if (sum > 21) {
        output = 'Busted...'
    }
    let p = document.createElement('p')
    p.innerText = output
    suggest.prepend(p)
})