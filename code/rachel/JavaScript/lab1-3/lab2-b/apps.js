let cardsDiv = document.getElementById('cards-div')
let cards = document.getElementsByClassName('card')
let adviceBtn = document.getElementById('advice')
let results = document.getElementById('results')
let card1 = document.getElementById('card1')
let card2 = document.getElementById('card2')
let card3 = document.getElementById('card3')

adviceBtn.addEventListener('click', function(){
    let total = parseInt(card1.value) + parseInt(card2.value) + parseInt(card3.value)
    console.log(total)

    if (total < 17) {
        let hitResult = document.createElement('hit')
        hitResult.innerText = `${total} - Hit`
        results.prepend(hitResult)
    } else if (total >= 17) {
        if (total >21) {
            let bustedResult = document.createElement('busted')
            bustedResult.innerText = `${total} - "Already Busted"`
            results.prepend(bustedResult)
        }
        if (total < 21) {
            let stayResult = document.createElement('stay')
            stayResult.innerText = `${total} - "Stay"`
            results.prepend(stayResult)
        }
        if (total === 21) {
            let blackjackResult = document.createElement('blackjack')
            blackjackResult.innerText = `${total} - "Blackjack!"`
            results.prepend(blackjackResult)
        }  
    }
})