let rot13= {
    'a':'n',
    'b':'o',
    'c':'p',
    'd':'q',
    'e':'r',
    'f':'s',
    'g':'t',
    'h':'u',
    'i':'v',
    'j':'w',
    'k':'x',
    'l':'y',
    'm':'z',
    'n':'a',
    'o':'b',
    'p':'c',
    'q':'d',
    'r':'e',
    's':'f',
    't':'g',
    'u':'h',
    'v':'i',
    'w':'j',
    'x':'k',
    'y':'l',
    'z':'m'
}

let userstring = prompt('Please enter a string:  ')
// '''alert(rot13[userstring])'''

let new_word = []
let newstring = new_word.join(userstring)
alert(newstring)

for (letter in newstring){
    new_word.append(rot13[letter])
}

alert(''.join(new_word))




