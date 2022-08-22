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

    // console.log("letter: " + letter)      // TEST
    // let char_index = alphabet_list.indexOf(letter)    // TEST
    // console.log("char_index: " + char_index)  // TEST
    // console.log("rot_index: " + rot_index)    // TEST
    // console.log("rot_char: " + rot_char)      // TEST
   
    return rot_char
}

// Prompt user for a string
let user_string = prompt("Enter a string: ")

// Define rotation factor
let rotation = 13

// Break string up into a list of individual characters
let user_char_list = []

// user_char_list = [user_string[i] for user_string in user_string]
for (let i=0; i<user_string.length;i++) {
    user_char_list += user_string[i]
}

// Loop through the user character list and call ROT Cipher function
let encrypted_string = ''

// for (char in user_char_list) {
for (let i=0; i<user_char_list.length;i++) {
        encrypted_string += rot_cipher(user_char_list[i],rotation)
}

// Print encrypted string
alert("Encrypted string: " + encrypted_string)