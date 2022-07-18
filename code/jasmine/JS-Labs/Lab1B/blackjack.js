let first_card = document.getElementById('card1')
let second_card = document.getElementById('card2')
let third_card = document.getElementById('card3')
let cards = document.getElementsByClassName('card')
let total = document.getElementById('points')
let button = document.getElementById('advice')


function addPoints(){

    
    

    if (points >= 17 && points < 21){
        return `{points} - "You should stay here"`
    } 
        else if (points === 21){
            return `{points} - "BlackJack!"`
    }
        else if (points > 21){
            return `{points} - "Busted! you lost"`
        }
    }

button.addEventListener('click', function(){
    let points = parseInt(first_card.value) + parseInt(second_card.value) + parseInt(third_card.value)
    console.log(points)
})
