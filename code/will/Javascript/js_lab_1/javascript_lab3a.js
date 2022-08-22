let nums = [5,0,8,3,4,1,6 ]

let total = 0


for (let num of nums){
    sumTotal = total + num
}

let answer = total / nums.length


user_input = []

let inputloop = true;
while (inputloop) {
    let input_num = prompt('Enter a number for a new average. Type done to get your result')
    if (input_num === 'done'){
        inputloop = false;
    } else {
        user_input.push(input_num)
    }
}

let final_sum = 0

for (let input of user_input){
    final_sum = final_sum + Number(input)
}

let final_average = final_sum / user_input.length

alert(final_average)