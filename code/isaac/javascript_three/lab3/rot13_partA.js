// ROT13 -- Python to JavaScript

// Create a function that accepts a message

// Part A

function rot13 (cipher) {
    var initialAlphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'// have a string of the initial alphabet
    var cipherAlphabet = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'// alphabet ciphered
    return cipher.replace(/[a-z]/gi, letter => cipherAlphabet[initialAlphabet.indexOf(letter)])// return indices
}

let userInput = prompt("Enter message: ")
alert(rot13(userInput))