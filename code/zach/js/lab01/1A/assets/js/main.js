let length = prompt('enter desired password length', 8)
let id = prompt('enter password features: [u]pper,[n]umbers,[s]ymbols \nex: uns or un')

switch (id) {
    case 'u':
        values = "ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz";
        console.log(id);
        break;
    case 'n':
        values = "abcdefghijklmnopqrstuvwxyz1234567890";
        console.log(id);
        break;
    case 's':
        values = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+";
        console.log(id);
        break;
    case 'un':
        values = "ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz1234567890";
        console.log(id);
        break;
    case 'us':
        values = "ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+";
        console.log(id);
        break;
    case 'ns':
        values = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+";
        console.log(id);
        break;
    case 'uns':
        values = "ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+";
        console.log(id);
        break;
    default:
        values = "abcdefghijklmnopqrstuvwxyz";
        console.log(id);
        break;
}

let password = '';

for (var i = 0; i < length; i++) {
    password = password + values.charAt(
        Math.floor(Math.random() * Math.floor(values.length - 1))
    );
}

alert(password)