let numtotext = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 
10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

let x = parseInt(prompt('Pick a whole numerical number between 0 and 999 to be converted to be converted to text.'))
if (x>=999) {
    alert('Pick a number between 0 and 999')
}
let tnref = 'a'

let statement = true
while (statement) {
    if (x >= 11 && x <= 20) {
        let teenref = numtotext[x]
        alert(teenref)
        break
    }

    if (x >= 0 && x <= 99) {
        let ones = x % 10
        let tens = Math.round((x - ones) )
        console.log(tens)
        
        let tref = numtotext[tens]
        let oref = numtotext[ones]
        if (ones === 0) {
            alert(tref)
            break   
        }
        if (tens === 0) {
            alert(oref)
            break
        }
        else {
            alert(tref+'-'+oref)
            break
        }
    }

    if (x >= 100 && x <= 999) {
        let ones = x % 10
        let huns = Math.floor(x / 100)
        let tens = Math.floor((x - huns * 100)/10)*10
        let teens = Math.round(x - huns * 100)
        console.log(ones, huns, tens, teens)
        // huns = Math.round((x - tens - ones) / 100)
        if (teens >= 10 && teens <= 20) {
            tnref = numtotext[teens]
        }
        
        let href = numtotext[huns]
        let tref = numtotext[tens]
        let oref = numtotext[ones]
        if (ones === 0 && tens ===0) {
            alert(href+'-hundred')
            break
        }
        if (tens === 0) {
            alert(href+'-hundred and '+oref)
            break
        }
        if (teens >= 11 && teens <= 20) {
            alert(href+'-hundred and '+tnref)
            break
        }
        if (ones === 0) {
            alert(href+'-hundred and '+tref)
            break
        }
        else {
            alert(href+'-hundred and '+tref+'-'+oref)
            break
        }
    }
}

