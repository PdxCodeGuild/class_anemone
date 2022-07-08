let nums = document.getElementById('nums')
let add = document.getElementById('addNum')
let del = document.getElementById('deleteNum')
let avg = document.getElementById('average')

// set nums array and set sum equal to 0
// let nums = []
// let sum = 0

// user message
alert("Enter as many numbers as you'd like. When you're finished, enter 'done', and the average of all of the numbers you entered will be displayed")

// fill nums array with numbers from user
while (true) {
    let number
    number = prompt("Enter a number or 'done' ")
    if (number === 'done') {
        break
    }
    nums.push(parseInt(number))
}

// sum all num in nums
for (let i = 0; i < nums.length; i++) {
    sum += nums[i]
}

// calc avg
let average = sum/nums.length

// print avg
alert(`Your average is ${average}.`)