var dict = {
    'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 
}

let score = []

let card = document.getElementsByClassName('card')
let cards = document.getElementById('cards')
let playerscore = document.getElementById('playerscore')
let next_card = document.getElementById('next_card')
let count = document.getElementById('count')

next_card.addEventListener('click', function(){
    let player_input = document.createElement('select')
    player_input.classList.add('card')
    player_input.innerHTML=` 
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
    <option value="K">King</option>    
    <option value="A">Ace</option>`

    playerscore.appendChild(player_input)
})

count.addEventListener('click', function() {
    let player_total = 0

    for (let i=0; i<card.length;i++) 

     
        
        player_total += parseFloat(dict[(card[i].value)])

    let player_score_value = document.createElement('p')
    player_score_value.innerText = player_total
    playerscore.prepend(player_score_value)

    if (player_total < 17 ) {
        playerscore.append("You need to hit")
    } else if (player_total >= 17 && player_total < 21) {
        playerscore.append("You should stay")
    } else if (player_total === 21) {
        playerscore.append("You win! Blackjack!")
    } else {
        playerscore.append('you lose')
    }
})





// function getsum(score) {
//     const total = score.reduce((acc, c) => acc + c, 0);
//     return total}

// const sum = getsum(score);


// if(sum > 21) {
//     window.alert("Busted")

// }
// else if(sum === 21){
//     window.alert("BLACKJACK!!")
// }
// else if(sum > 17){
//     window.alert("You should stay")
// }
// else if (sum < 17){
//     window.alert("You should hit")
// }


