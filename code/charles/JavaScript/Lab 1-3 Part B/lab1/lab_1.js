let numtotext = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 
10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}



let convert = document.getElementById("convert")


convert.addEventListener('click', function() {
    let body = document.getElementById("body")
    let x = document.getElementById('number')
    x = parseInt(x.value)
    
    let answer = ''
    let ones = 0
    let teens = 0
    let tens = 0
    let huns = 0
     
    let oref = ''
    let teenref = ''
    let tref = ''
    let href = ''
    if (x >= 999) {
    alert('Pick a number between 0 and 999')
}
       

    if (x >= 11 && x <= 20) {
        teenref = numtotext[x]
        answer = teenref
        console.log('p', answer, oref, teenref, href, tref)
    }
    else if (x >= 0 && x <= 99) {
        ones = x % 10
        tens = Math.round((x - ones))
        tref = numtotext[tens]
        oref = numtotext[ones]

        if (ones === 0) {
            answer += tref   
        }
        else if (tens === 0) {
            answer += oref
        }
        else {
            answer += (tref+'-'+oref)
        }
    }

    else if (x >= 100 && x <= 999) {
        
        ones = x % 10
        huns = Math.floor(x / 100)
        tens = Math.floor((x - huns * 100)/10)*10
        teens = Math.round(x - huns * 100)
        href = numtotext[huns]
        tref = numtotext[tens]
        oref = numtotext[ones]
        teenref = numtotext[teens]
        console.log(x,ones,huns,tens,teens)

        if (teens >= 11 && teens <= 19) {
            answer += href+'-hundred and '+teenref
        }
        
        else if (ones === 0 && tens ===0) {
            answer += href+'-hundred'
        }

        else if (tens === 0) {
            answer += href+'-hundred and '+oref
        }

        else if (ones === 0) {
            answer += href+'-hundred and '+tref
        }
        else {
            answer += href+'-hundred and '+tref+'-'+oref
        }
    }
    
    let resultP = document.createElement('p')
    resultP.innerText = answer
    body.prepend(resultP)
    
})

