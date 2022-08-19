let nums = document.getElementsByClassName('num')
let addNum = document.getElementById('add-num')
let numDiv = document.getElementById('num-div')
let calcAvgBtn = document.getElementById('calc-avg')
let results = document.getElementById('results')

addNum.addEventListener('click', function() {
    let newNum = document.createElement('input')
    newNum.type = 'number'
    newNum.classList.add('num')
    numDiv.appendChild(newNum)
   
})

calcAvgBtn.addEventListener('click', function() {
    let answer = 0
    for (let i=0; i<nums.length; i++) {
        if (nums[i].value === "") {
            nums[i].valie = 0
        }
        answer += parseInt(nums[i].value)
        avg_answer = answer / nums.length
    }

    let answer_final = document.createElement('p')
    answer_final.innerText = avg_answer
    results.prepend(answer_final)
})  