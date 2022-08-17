var dict = {
    'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 
}

let score = []

let input1 = prompt("Please enter your first card's value")
let input2 = prompt("Please enter your second card's value")
let input3 = prompt("Please enter your third card's value")


console.log(dict.score.push(input1))
console.log(dict.score.push(inpu2))
console.log(dict.score.push(input3))


function getsum(score) {
    const total = score.reduce((acc, c) => acc + c, 0);
    return total}

const sum = getsum(score);


if(sum > 21) {
    window.alert("Busted")

}
else if(sum === 21){
    window.alert("BLACKJACK!!")
}
else if(sum > 17){
    window.alert("You should stay")
}
else if (sum < 17){
    window.alert("You should hit")
}


