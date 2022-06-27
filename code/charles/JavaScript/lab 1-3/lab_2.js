let statement = true
while (statment) {
    let input = prompt('Please enter a 16 digit card number to verify.')
    if (input.length <16) {
        alert('Not a correct amount of digits.')
        continue
    }
    else {
        alert(validation(input))
        statement = false
    }
}

function validation(verify) {
    let ccard = verify
    let ccardlist = []
    for (let i = 0; i<ccard.length; i++) {
        ccardlist.push(parshInt(ccard[i]))
    }
    let ccardpop = parseInt(ccardlist.pop())

    let ccardr = ccardlist.reverse()

    for (i=0; i<ccardr/2+1; i++) {
        ccard[i *2] = ccardr[i*2] + ccardr[i*2]
        console.log(ccard[i *2])
    }

    for (i=0; i<ccardr.length; i++) {
        if (ccardr[i]>9) {
            ccardr[i] = parseInt(ccardr[i]) - 9
        }
    }
    let a = 0
    for (i=0;i<ccardr.length;i++) {
        a += ccardr[i]
    }

    let confirm = a % 10
    if (confirm === ccardpop) {
        alert('Valid')
    }
    else {
        alert('Invalid')
    }
}

