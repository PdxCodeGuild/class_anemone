var userinput = prompt("Please select pock, paper, or scissors: ")
var selection = ['rock','paper','scissors']
var compinput = selection[Math.floor(Math.random()*selection.length)]

if (userinput == compinput){
    alert("Computer chose the same: Its a tie")
}
else if (userinput == 'rock' && compinput == 'paper'){
    alert("Computer chose paper: You lose")
}
else if (userinput == 'rock' && compinput == 'scissors'){
    alert("Computer chose scissors: You win")

}
else if (userinput == 'paper' && compinput == 'scissors'){
    alert("Computer chose scissors: You lose")
}
else if (userinput == 'paper' && compinput == 'rock'){
    alert("Computer chose rock: You lose")
    
}
else if (userinput == 'scissors' && compinput == 'paper'){
    alert("Computer chose paper: You win")
}
else if (userinput == 'scissors' && compinput == 'rock'){
    alert("Computer chose rock: You lose")
}