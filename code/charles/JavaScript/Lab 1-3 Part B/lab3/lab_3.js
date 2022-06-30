let index1 = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
                'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26} 

let index2 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m',
                14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'} 


let enigma = document.getElementById('enigma')
let deni = document.getElementById('deni')


enigma.addEventListener('click', function () {
    let cypher = ''
    let data = document.getElementById('data')
    data = data.value
    let shift = document.getElementById('num')
    shift=parseInt(shift.value)
    
    
    for (i=0; i<data.length; i++) {
        if (data[i] === ' ') {
            cypher += ' '
            
        } else if (data[i] === '0'|data[i] === '1'|
        data[i] === '2'|data[i] === '3'|
        data[i] === '4'|data[i] === '5'|
        data[i] === '6'|data[i] === '7'|
        data[i] === '8'|data[i] === '9') {
            cypher += data[i]
        }
        
        else {
            let num = index1[data[i]] + shift
            num = num % 26
            if (num === 0) {
                num = 26
            }
            let letter = index2[num]
            cypher += letter
            
        }
    }
    let code = document.createElement('p')
    code.innerText = cypher
    body.prepend(code)
})

deni.addEventListener('click', function() {
    let cypher2 = ''
    let data = document.getElementById('data')
    data = data.value
    let shift = document.getElementById('num')
    let shift2 = parseInt(shift.value)

    for (i=0; i<data.length; i++) {
        if (data[i] === ' ') {
            cypher2 += ' '
        } else if (data[i] === '0'|data[i] === '1'|
        data[i] === '2'|data[i] === '3'|
        data[i] === '4'|data[i] === '5'|
        data[i] === '6'|data[i] === '7'|
        data[i] === '8'|data[i] === '9') {
            cypher2 += data[i]
        }
        else {
            let num = index1[data[i]] - shift2
            if (num < 1) {
                num = num + 26
            }
            let letter = index2[num]
            cypher2 += letter
        }
    }
    let code = document.createElement('p')
    code.innerText = cypher2
    body.prepend(code)
})

// let enter = true

// while (enter) {
//     let ud = prompt('Would you like to encrypt or decrypt? ')
//     let yes = ['yes', 'yea', 'sure', 'why not', 'ya']
//     let no = ['no', 'na', 'nope']    
//     let en = ['encrypt', 'encryption', 'up']
//     let de = ['decrypt', 'decryption', 'down']
    
//     for (i=0; i<en.length;i++) {
//         if (ud === en[i]) {
//             let phrase1 = prompt('Please enter a phrase to encrypt.')
//             console.log(phrase1)
//             let shift3 = prompt('Please enter the numerical number you would like to encrypt.')
//             console.log(shift3)
//             let encode = encrypt(phrase1, shift3)
//             alert(encode)
//         }
//     }
    
//     for (i=0; i<de.length;i++) {
//         if (ud === de[i]) {
//             let phrase2 = prompt('Please enter a phrase to decrypt.')
//             let shift4 = prompt('Please enter the numerical number you would like to decrypt.')
//             let decode = decrypt(phrase2, shift4)
//             alert(decode)
//         }
//     }
    
//     let again = prompt('Would you like to try something else yes or no.')
    
//     for (i=0; i<yes.length;i++) {
//         if (again === yes) {
//             continue
//         }
//     }
    
//     for (i=0; i<en.length;i++) {
//         if (again === no[i]) {
//             alert('Goodbye Stranger')
//             enter = false
//         }
//     }
// }