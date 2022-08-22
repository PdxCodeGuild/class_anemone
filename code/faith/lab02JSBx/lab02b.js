// let firstcard = prompt('What is your first card?:  ')
// let secondcard = prompt('What is your second card?:  ')
// let thirdcard = prompt('What is your third card?:  ')

let cards = {
    'A':1,
    'J':10,
    'K':10,
    'Q':10,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10
    }
    
// let fc = cards[firstcard]
// let sc = cards[secondcard]
// let tc = cards[thirdcard]

// let hand = fc+sc+tc

// result.append(hand)



let card = document.getElementsByClassName('card')
let subbtn = document.getElementById('submit')
let result = document.getElementById('result')
let carddropdown = document.getElementById('cards')
let newcardBtn = document.getElementById('newcard') 

newcardBtn.addEventListener('click', function() {
    let newlist = document.createElement('select')
    newlist.classList.add('card')
    newlist.innerHTML= `
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
    <option value="J">J</option>
    <option value="Q">Q</option>
    <option value="K">K</option>`
})




subbtn.addEventListener('click', function() {
    let hand = 0

    for (let i=0; i<card.length;i++) 


        hand += parseInt(cards[(card[i].value)])

    
    
    let resultx = document.createElement('x')
    resultx.innerText = hand
    result.prepend(resultx)





    if (hand == 21){
        result.append('Blackjack')}
    else if (hand >= 21){
        result.append('Already busted')}
    else if (hand <17){
        result.append('Hit')}
    else if (hand >= 17 && hand < 21){
        result.append('Stay')}


    })











// let btn=document.getElementById('Submit')
// btn.addEventListener('click', function(){
//     let distance = document.getElementById('input')
//     let input = distance.value
//     let unit = document.getElementById('unit')
//     let unit2 = document.getElementById('unit2')
//     let number = convert(parseInt(input),unit.value,unit2.value)
// let conversion = document.getElementById('conversion')
// conversion.innerHTML= number
// })