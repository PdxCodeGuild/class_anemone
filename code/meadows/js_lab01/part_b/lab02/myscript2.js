let RocBTN = document.getElementById('BTN')
let hitDiv = document.getElementById('results')

RocBTN.addEventListener('click', function(){
    let RC13 = document.getElementById('RC-13')
    RC13 = RC13.value
    console.log(RC13)
    var roc_13 = RC13.replace(/[a-z]/g,function(values){

        var dict = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z',
        'n': 'a', 'o': 'b','p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}
    
        return dict[values]
    
    })

    let resultP = document.createElement('p')
    resultP.innerText = roc_13
    hitDiv.prepend(resultP)
})