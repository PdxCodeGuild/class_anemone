let cipherDiv = document.getElementById('cipher-div')
let cipher = document.getElementById('user-word')
let cipherBtn = document.getElementById('cipher')
let results = document.getElementById('results')

cipherBtn.addEventListener('click', function(){
    let phrase = Array.from(cipher.value)
    let abc = Array.from('abcdefghijklmnopqrstuvwxyz')
    let newWord = ''

    for (let letter of phrase) {
        let letterIndex = abc.indexOf(letter)
        let newIndex = letterIndex + 13
        if (newIndex > 25) {
            newIndex -= 26
        }
        let wordCipher = abc[newIndex]
        newWord +=wordCipher
    }

    let result = document.createElement('p')
    result.innerText = newWord
    results.prepend(result)
})
