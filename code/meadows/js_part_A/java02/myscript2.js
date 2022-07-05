
let input = prompt("Enter a word: ").toLowerCase()
var roc_13 = input.replace(/[a-z]/g,function(values){ // replacing a-z in all inputs with /g (global), and making it replace the key with str ex: input --> rock13 keys . replace all. roc13[values] return dict[values]

    var dict = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z',
    'n': 'a', 'o': 'b','p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}

    return dict[values]

})

alert(" You word " + input +" became " + roc_13)
