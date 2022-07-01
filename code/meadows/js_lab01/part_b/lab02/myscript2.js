Rocky = document.getElementsByClassName('Rock')
RockBTN = document.getElementById('rock-result')
RockDiv = document.getElementById('rock-div')

RockBTN.addEventListener('click', function() {

    let resultP = document.createElement('p')
    resultP.innerText.replace(/[a-z]/g,function(values){ 
        var dict = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z',
    'n': 'a', 'o': 'b','p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}

    return dict[values]
    })
    RockDiv.prepend(resultP)
})