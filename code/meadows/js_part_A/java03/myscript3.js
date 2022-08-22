var card = prompt("Enter Credit Card Number: ")

let myFunc = num => Number(num)

var intArr = Array.from(String(card), myFunc)
var intArr2 = [...intArr]

let hold = intArr.pop()

let Reverse = intArr2.reverse()

function everyOther(multArray) {
    for (var i = 1; i < multArray.length; i+=2) {
        multArray[i] *= 2
    }
    return multArray
}

let doubleReverse = everyOther(Reverse)
let dubReverse = []

let Reversedub = dubReverse.concat(doubleReverse)

function SubNum(subArray) {
    for (var i = 0; i < subArray.length; i++) {
        if (subArray[i] >= 10){
            subArray[i] = subArray[i] - 9
        }
    }
    return subArray
}

let subNum = SubNum(Reversedub)

let sum=0
for(let i = 0; i < subNum.length; i++){
    sum += subNum[i]
}

let numSum = sum / intArr2.length

if ( Math.floor(numSum)===hold) {
    alert("Your Credit Card is Valid")
}
else {
    alert("Your Credit Card is NOT valid")
}