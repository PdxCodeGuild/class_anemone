let statement = true
let input = prompt('Please enter a 16 digit card number to verify.')
function validation(verify) {
    let ccard = verify
    let ccardd =[]
    let ccardlist = []
    for (let i = 0; i<ccard.length; i++) {
        ccardlist.push(parseInt(ccard[i]))
    }
    console.log(ccardlist)

    let ccardpop = ccardlist.pop()
    console.log(ccardpop)
    let ccardr = ccardlist.reverse()
    console.log(ccardr)
    let a = 0
     
    
    for (i=0; i<ccardr.length/2+1; i++) {
        ccardd.push(ccardr[i*2] + ccardr[i*2])  
    } 
    for (i=0; i<ccardr.length/2+4; i+=1) {
        ccardr.splice(i, 1)
    }
   
    ccardd.pop()
    
    for (i=0; i<ccardd.length; i++) {
        dd = ccardd[i]
        r= ccardr[i]
        if (dd>9) {
            dd = dd-9
            ccardd[i] = dd
        }
        else {
            continue
        }
    }
    
    
    for (i=0;i<ccardd.length;i++) {
        console.log(ccardd[i])
        a += ccardd[i]
        console.log(a)
    }
    for (i=0;i<ccardr.length;i++) {
        console.log(ccardr[i])
        a += ccardr[i]
        
        console.log(a)
    }
    
    
    
    let confirm = a % 10 

    if (confirm === ccardpop) {
        alert('Valid')
    }
    else {
        alert('Invalid')
    }
}
while (statement) {
    if (input.length <16) {
        alert('Not a correct amount of digits.')
        input = prompt('Please enter a 16 digit card number to verify.')
    }
    else {
        validation(input)
        statement = false
    }
}


