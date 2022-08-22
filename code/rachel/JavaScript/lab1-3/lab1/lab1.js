let nums = [5, 0, 8, 3, 4, 1, 6]

let newTotal = 0

for (let num of nums) {
    newTotal = newTotal + num
}

let average = newTotal / nums.length
// console.log(average)

let nums2 = []

let invalidInput = true;
while (invalidInput) {
    let num2 = prompt('Enter a number of "done": ');
    if (num2 === 'done') {
        invalidInput = false;
    } else {
        nums2.push(num2)
    }
}

let newTotal2 = 0

for (let num of nums2) {
    newTotal2 = newTotal2 + Number(num)
}

let average2 = newTotal2 / nums2.length
alert(average2)