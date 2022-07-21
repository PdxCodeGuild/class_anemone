// ROT13 -- Python to JavaScript

// Create a function that accepts a message

// Part A

function rot13 (cipher) {
    var initialAlphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'// have a string of the initial alphabet
    var cipherAlphabet = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'// alphabet ciphered
    return cipher.replace(/[a-z]/gi, letter => cipherAlphabet[initialAlphabet.indexOf(letter)])// return indices
}



// Part B
let encodeBtn = document.getElementById('encode')

encodeBtn.addEventListener('click', function() {
    let inputMsg = document.getElementById('secret')
    let secretMsg = rot13(inputMsg.value)
    let hiddenMsg = document.getElementById('message')
    hiddenMsg.innerText = `${secretMsg}`
})  
    




//-------------------------------------//

// Part B

// let secretMsg = document.getElementById('secret')
// let encodeMsg = rot13(secretMsg).document.getElementById('message')


// encodeBtn.addEventListener('click', function() {
//     displayMsg = encodeMsg
//     return displayMsg
// })



