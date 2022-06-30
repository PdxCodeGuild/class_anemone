let statement = true

let validate = document.getElementById('validate')

validate.addEventListener('click', function() {
    let card = document.getElementById('cardnum')
    
    let body = document.getElementById('body')
    card = card.value
    let ccard = []
    for (i=0;i<16;i++) {
        ccard[i]=parseInt(card[i])   
    }
    let ccardpop = ccard.pop()
    let ccardr = ccard.reverse()
    let ccardd =[]
    let a = 0
    let valid = ''
    
    if (ccard.length === 16) {
        alert('Not a correct amount of digits.')
    }

    for (i=0; i<ccardr.length/2+1; i++) {
        ccardd.push(ccardr[i*2] + ccardr[i*2]) 
    } 
    for (i=0; i<ccardr.length/2+4; i+=1) {
        ccardr.splice(i, 1)  
    }
    
    ccardd.pop()
    
    for (i=0; i<ccardd.length; i++) {
        let dd = ccardd[i]
        if (dd>9) {
            dd = dd-9
            ccardd[i] = dd
        }
    }
    
    for (i=0;i<ccardd.length;i++) {
        a += ccardd[i]   
    }
    for (i=0;i<ccardr.length;i++) {
        a += ccardr[i]   
    }
  
    let confirm = a % 10 
    
    if (confirm === ccardpop) {
        valid += 'Valid'
    }
    else if (confirm != ccardpop) {
        valid +='Invalid'
    }

    let result = document.createElement('p')
    result.innerText ='Your card Number is '+valid
    body.prepend(result)

})


