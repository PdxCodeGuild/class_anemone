const digits = '0123456789'
const letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
const specChars = '!@#$%^&*'
const allChars = digits + letters + specChars

let code = ''
n = prompt('password length: ')
while (code.length < parseInt(n)) {randIndex = Math.floor(Math.random()*allChars.length)
    console.log(randIndex)
    console.log(allChars[randIndex])
    code += allChars[randIndex]
}
if (code !== '') {
    alert(code)
}

    