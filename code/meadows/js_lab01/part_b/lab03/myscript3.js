let hitDiv = document.getElementById('results')
let CC = document.getElementById('CC')

//CC number used -- 4556737586899855 ( python lab Lab 6)

CC.addEventListener('click', function(){
    let card = document.getElementById('cards')
    card = card.value
    console.log(card)
    let myFunc = num => Number(num)

    var intArr = Array.from(String(card), myFunc)
    var intArr2 = [...intArr]

    let hold = intArr.pop()

    let Reverse = intArr.reverse()
    console.log(Reverse)
    function everyOther(multArray) {
        for (var i = 0; i < multArray.length; i+=2) {
            multArray[i] *= 2
        }
        return multArray
    }

    let doubleReverse = everyOther(Reverse)
    let dubReverse = []

    let Reversedub = dubReverse.concat(doubleReverse)
    console.log(Reversedub)
    function SubNum(subArray) {
        for (var i = 0; i < subArray.length; i++) {
            if (subArray[i] >= 10){
                subArray[i] = subArray[i] - 9
            }
        }
        return subArray
    }

    let subNum = SubNum(Reversedub)
    console.log(subNum)

    let sum=0
    for(let i = 0; i < subNum.length; i++){
        sum += subNum[i]
    }

    lastNum = sum%10
    console.log(lastNum)

    if ( lastNum===hold) {
        Decide = "Your Credit Card is Valid"
    }
    else {
        Decide = "Your Credit Card is NOT valid"
    }
    let resultP = document.createElement('p')
    resultP.innerText = Decide
    hitDiv.prepend(resultP)
})