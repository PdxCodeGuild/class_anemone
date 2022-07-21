let phrase = Array.from(prompt("Enter a string: "))

let abc = Array.from('abcdefghijklmnopqrstuvwxyz')

let newWord = ''

for (let letter of phrase) {
    let letterIndex = abc.indexOf(letter)
    let new_index = letterIndex + 13
    if (new_index > 25) {
        new_index -= 26
    }
    let cipher = abc[new_index]
    newWord += cipher
    // console.log(cipher)
}
alert(newWord) 

