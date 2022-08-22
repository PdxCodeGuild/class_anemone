const computerChoice = document.getElementById('comp-input');
const userChoice = document.getElementById('user-input');
const resultChoice = document.getElementById('result');
const variable = document.querySelectorAll('button');
 
let userSelect
let compSelect
let result

variable.forEach(variable => variable.addEventListener('click', (e) => {
    userSelect = e.target.id
    userChoice.innerHTML = userSelect
    generateCompOutput()
    getResult()
    
}))

function generateCompOutput() {
    const randomSelect = Math.floor(Math.random() * 3) + 1

    if (randomSelect === 1) {
        compSelect = 'rock'
    }
    if (randomSelect === 2) {
        compSelect = 'scissors'
    }
    if (randomSelect === 3) {
        compSelect = 'paper'
    }
    // console.log(compSelect)
    // console.log(userSelect)
    computerChoice.innerHTML = compSelect
}

function getResult() {
    if (compSelect === userSelect) {
        result = "Its a Tie!!"
    }
    if (compSelect === 'rock' && userSelect === 'paper') {
        result = "You WIN!!"
    }
    if (compSelect === 'rock' && userSelect === 'scissors') {
        result = "You Lose"
    }
    if (compSelect === 'scissors' && userSelect === 'rock') {
        result = "You WIN!!"
    }
    if (compSelect === 'scissors' && userSelect === 'paper') {
        result = "You Lose!!"
    }
    if (compSelect === 'paper' && userSelect === 'scissors') {
        result = "You Win!!"
    }
    if (compSelect === 'paper' && userSelect === 'rock') {
        result = "You Lose"
    }
    // console.log(result)
    resultChoice.innerHTML = result
    
}