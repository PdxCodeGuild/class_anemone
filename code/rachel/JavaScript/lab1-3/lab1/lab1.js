let nums = [5, 0, 8, 3, 4, 1, 6]

let newTotal = 0

for (let num of nums) {
    newTotal = newTotal + num
    console.log(newTotal)
}

let average = newTotal / nums.length
console.log(average)
alert(average)