let nums = document.getElementsByClassName('num')
let addNumBtn = document.getElementById('add-num')
let numDiv = document.getElementById('num-div')
let calcAvgBtn = document.getElementById('calc-avg')
let results = document.getElementById('results')

addNumBtn.addEventListener('click', function() {
    let newNum = document.createElement('input')
    newNum.type = 'number'
    newNum.classList.add('num')

    let newNumRemoved = document.createElement('button')
    newNumRemoved.innerText = 'x'
    newNumRemoved.addEventListener('click', function(){
        newNum.remove()
        newNumRemoved.remove()
    })

    numDiv.appendChild(newNum)
    numDiv.appendChild(newNumRemoved)
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

    let result = document.createElement('p')
    result.innerText = avg_answer
    results.prepend(result)
})  