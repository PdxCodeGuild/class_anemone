// Lab01 ** Part B - Blackjack Advice
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


let cards = document.getElementsByClassName('card')
let calculateBtn = document.getElementById('calculate')
let resultsDiv = document.getElementById('results')
let cardDiv = document.getElementById('card-div')
let addCardBtn = document.getElementById('add-card') 

addCardBtn.addEventListener('click', function() {
    let newNum = document.createElement('select')
    newNum.classList.add('card')
    newNum.innerHTML=`
        <option value="A">Ace</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
        <option value="J">Jack</option>
        <option value="Q">Queen</option>
        <option value="K">King</option>`

    let newNumRemove = document.createElement('button')
    newNumRemove.innerText = '×'
    newNumRemove.addEventListener('click', function() {
        newNum.remove()
        newNumRemove.remove()
    })

    cardDiv.appendChild(newNum)
    cardDiv.appendChild(newNumRemove)
})

// Add card values and return advice on what to do next
// Assuming aces are always worth one point

calculateBtn.addEventListener('click', function() {
    let hand_total = 0

    for (let i=0; i<cards.length;i++) 

        // cards[i].value: get the face value of the card the user entered (Ace,1-10,Jack,Queen,King)...
        // card_values[]: ...then look up the point value for that card in the card_values object
        
        hand_total += parseFloat(card_values[(cards[i].value)])

    let resultP = document.createElement('p')
    resultP.innerText = hand_total
    resultsDiv.prepend(resultP)

    if (hand_total < 17 ) {
        resultsDiv.append("...Hit")
    } else if (hand_total >= 17 && hand_total < 21) {
        resultsDiv.append("...Stay")
    } else if (hand_total === 21) {
        resultsDiv.append("...Blackjack!")
    } else {
        resultsDiv.append('...Already busted')
    }
})
