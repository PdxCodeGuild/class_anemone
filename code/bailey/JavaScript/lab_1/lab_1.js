var card = prompt("Please input credit card number: ");

var cardArr = String(card).split("").map((card)=>{
    return Number(card)
  })

console.log(cardArr)

check_digit = cardArr.pop();

console.log(check_digit)

cardArr.reverse();

console.log(cardArr);

for (let i = 0; i < cardArr.length; i+=2){
    cardArr[i] = cardArr[i] * 2
}

console.log(cardArr)

for (let i=0; i<cardArr.length; i++){
    if (cardArr[i] > 9){
        cardArr[i] = cardArr[i] - 9
    }
}

console.log(cardArr)

let total = 0

for (let i = 0; i<cardArr.length; i++){
    total += cardArr[i]
}
console.log(total)
total = total % 10
console.log(total)

if (total === check_digit){
    alert("True, Valid!")
}else{
    alert("Card number not valid")
}
