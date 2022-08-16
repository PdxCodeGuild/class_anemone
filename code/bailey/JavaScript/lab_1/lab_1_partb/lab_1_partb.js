// var card = prompt("Please input credit card number: ");

let checkCard = document.getElementById("check_card");


checkCard.addEventListener('click', function() {
    var card = document.getElementById("user_input").value;
    let resultsDiv = document.getElementById('results')
    console.log(card)
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
        let resultP = document.createElement('p')
        resultP.innerText = `${card} was a valid card number!`
        resultsDiv.prepend(resultP)
    }else{
        let resultP = document.createElement('p')
        resultP.innerText = `${card} was not a valid card number.`
        resultsDiv.prepend(resultP)
    }
})
