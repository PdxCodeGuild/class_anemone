

let values = {
    prompts: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
};


function generatePassword() {
    var container = "" + values.prompts;
    var result = "";
    
    let characterLength = prompt("Enter password length between 1 and 100: ");
    if(isNaN(characterLength) || characterLength < 0) {
        alert("Character length has to be a number, 1 - 100. Please try again.");
    }

    for (let i = 0; i < characterLength; i++) {
        result += container[Math.floor(Math.random()*container.length)]
    };
    return result;
}

var myanswer = document.getElementById('result');
myanswer.innerHTML = generatePassword();


// getNums.addEventListener('click', function(){
//     let answer = generatePassword()
//     result.innerText = answer
// })

