// let u_name = prompt("Enter your name")
// alert("Hello " + u_name + "!")
// let num1 = prompt('enter number: ')
// let num2 = prompt("enter number: ")
// num1 = parseInt(num1)
// num2 = parseInt(num2)
// alert(num1 + num2)

// let temp = Math.floor(50 + Math.random()*50)
// alert(temp)
// if (temp < 60) {
//     alert("cold outside")
//     let y = 0
// } else if (temp < 80) {
//     alert("warm outside")
//     let y = 1
// } else {
//     alert("hot outside")
// }
// alert(y)

// let fruits = ['apple', 'mango', 'orange']
// fruits.push('pear')
// console.log(fruits.slice(fruits.indexOf('apple'),0))


// alert(fruits)

// let i = 0
// while (i < 5) {
//     i++
//     alert(i)
// }
// names = ['jack','jill','joe']
// for (let i=0; i < names.length; i++) {
//     alert(names[i])
// }

// let fruits = {
//     'pear': .70,
//     'apple': .55,
//     'orange': .25
// }

// for (let key in fruits) {
//     alert(fruits[key])
// }

// for (let fruit of fruits) {
//     console.log(fruit)
// }

// fruits.forEach(function(fruit) {
//     alert(fruit)
// })

// let contact = {
//     f_name: 'Jane',
//     l_name: 'Doe',
//     age: 34
// }

// let library_user = {
//     first_name: 'Jane',
//     last_name: 'Smith',
//     age: 20,
//     books: [{
//         title: 'A Wrinkle in Time',
//         author: 'Madeleine L\'Engle',
//         published: 1962
//     },{
//         title: 'The Giving Tree',
//         author: 'Shel Silverstein',
//         published: 1964
//     }]
// }



// let results = []
// for (let i = 0; i < library_user.books.length; i++)
//     if (library_user.books[i].author === 'Madeleine L\'Engle') {
//     }
// console.log(results)

// function add(a, b) {
//     return a * b 
// }
// let x = Math.floor(1 + Math.random()*10)
// let y = Math.floor(1 + Math.random()*10)
// console.log('x: ' + x)
// console.log('y: '+ y)
// console.log(add(x,y))

// function randomNumber(x,y) {
//     let random_number = Math.floor(x + Math.random()*y)
//     return random_number
// }

// let x = randomNumber(1,10)
// console.log(x)

// function randomNumber(x,y) {
//     let z = y-x
//     let random_number = Math.floor(x + Math.random()*z)
//     return random_number
// }

// // test = Math.floor(18 + Math.random()*44)

// let x = prompt("pick start of range: ")
// let y = prompt("pick end of range: ")
// console.log(x)
// console.log(y)
// let rand = randomNumber(x,y)



// console.log(rand)


// class ATM {
//     constructor(balance=0) {
//         this.balance = balance
//     }
//     get_balance() {
//         return this.balance
//     }
// }

// let atm = new ATM(5.0)
// alert(atm.get_balance())

// let atm = {
//     balance: 5.0,
//     get_balance: function() {
//         return this.balance
//     }
// }

// alert(atm.get_balance())