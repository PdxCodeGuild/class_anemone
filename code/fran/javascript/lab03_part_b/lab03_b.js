// Lab03 - ROT Cipher
// Fran Kappes


// Define ROT cipher function
function rot_cipher(letter, rotation) {

    // Define alphabet list
    let alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    // Determine ROTn character
    let rot_index = 0
    if (alphabet_list.indexOf(letter) < 13) {
        rot_index = alphabet_list.indexOf(letter) + 13
    } else {
        rot_index = alphabet_list.indexOf(letter) - 13
    }

    let rot_char = alphabet_list[rot_index]

    // console.log("begin function")       // TEST
    // console.log("letter: " + letter)      // TEST
    // let char_index = alphabet_list.indexOf(letter)    // TEST
    // console.log("char_index: " + char_index)  // TEST
    // console.log("rot_index: " + rot_index)    // TEST
    // console.log("rot_char: " + rot_char)      // TEST
    // console.log("end function")         // TEST
   
    return rot_char
}

let userString = document.getElementById('user-string')
let encodeBtn = document.getElementById('encode')
let resultsDiv = document.getElementById('results')

encodeBtn.addEventListener('click', function() {

    // Define rotation factor
    let rotation = 13

    // Break string up into a list of individual characters
    let user_char_list = []

    for (let i=0; i<userString.value.length;i++) {
        user_char_list += userString.value[i]
    }

    // Loop through the user character list and call ROT Cipher function
    let encrypted_string = ''

    for (let i=0; i<user_char_list.length;i++) {
        encrypted_string += rot_cipher(user_char_list[i],rotation)
        }

    let resultP = document.createElement('p')
    resultP.innerText = encrypted_string
    resultsDiv.prepend(resultP)

})
