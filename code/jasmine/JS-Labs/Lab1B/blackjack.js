let first_card = document.querySelector("#first_card")
let second_card = document.querySelector("#second_card")
let third_card = document.querySelector("#third_card")


let card_one = {
    'a': 11,
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'J': 10,
    'q': 10,
    'Q': 10,
    'k': 10,
    'K': 10
}
let card_two = {
    'a': 1,
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'J': 10,
    'q': 10,
    'Q': 10,
    'k': 10,
    'K': 10
}



let btn = document.querySelector("#btn")
btn.addEventListener("click", function () {
    let points = document.querySelector("#points")

    total = card_one[first_card.value] + card_one[second_card.value] + card_one[third_card.value]

    if (total < 17) {

        points.innerText = `You should choose another card with ${total}`

    }
    else if (17 <= total && total < 21) {
        points.innerText = `You should stay here! ${total}`
    }
    else if (total === 21) {
        points.innerText = `${total} Blackjack! You win`
    }
    else if (total > 21) {
        total = card_two[first_card.value] + card_two[second_card.value] + card_two[third_card.value]

        if (total < 17) {
            points.innerText = `You should choose another card with ${total}`
        }
        else if (17 <= total && total < 21) {
            points.innerText = `You should stay here! ${total}`
        }
        else if (total === 21) {
            points.innerText = `${total} BLACKJACK`
        }
        else if (total > 21) {
            points.innerText = `${total} BUSTED. You lose...`
        }
    }


})
