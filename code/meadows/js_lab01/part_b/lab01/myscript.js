let cards = document.getElementsByClassName('card')
let cardDiv = document.getElementById('card-Div')
let HitBTN = document.getElementById('hit')
let hitDiv = document.getElementById('results')
let dealerDiv = document.getElementById('info')


HitBTN.addEventListener('click', function() {
    let dealer = 0
    for (let i=0; i<cards.length; i++){
        for (let i=0; i<cards.length;i++) {
            if (cards[i].value === "A") {
                cards[i].value = 1
            }
            else if (cards[i].value ==="Q" || cards[i].value ==="K" || cards[i].value ==="J") {
                cards[i].value = 10
            }
            else if (cards[i].value === "") {
                cards[i].value = 0
            }
            else if (cards[i].value > 10) {
                alert("PICK Q,K,J OR 2-10, this play was invalid")       
            }
        }
        dealer += parseInt(cards[i].value)
    }
    
    if (dealer < 17){
        Decide = "I would HIT!!"
    }
    else if(dealer >= 17 && dealer < 21) {
        Decide = "I would STAY!"
    }
    else if(dealer === 21) {
        Decide = "YOU WON! BLACK JACK BABY!"
    }
    else if(dealer >21) {
        Decide = "BUST..GG, you LOSE!"
    }
    let resultP = document.createElement('p')
    let dealerP = document.createElement('o')
    resultP.innerText = dealer
    dealerP.innerText = Decide
    hitDiv.prepend(resultP)  
    hitDiv.prepend(dealerP)
})