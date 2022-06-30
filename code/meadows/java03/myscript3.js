var card = prompt("Enter Credit Card Number: ")

let myFunc = num => Number(num)

var intArr = Array.from(String(card), myFunc)

hold = []
hold = intArr.pop()

Reverse = intArr.reverse()

// for (let i = 0; i < Reverse.length; i++) {
//     console.log(Reverse[i] *= 2)
// }

function everyOther(ccArray) {
    for (var i = 1; i < ccArray.length; i+=2) {
        ccArray[i] *= 2;
    }
    return ccArray;
}

doubleReverse = everyOther(Reverse)

function DivNum(divArray) {
    for (var i = 0; i < divArray.lenght; i++) {  // not subtracting
        if (i >= 10){
            divArray - 9;
        }
    }
    return divArray;
}

console.log(DivNum(doubleReverse))