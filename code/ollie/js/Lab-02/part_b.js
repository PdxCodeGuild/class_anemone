let nums = document.getElementById('nums')
let num = document.getElementsByClassName('num')
let add = document.getElementById('addBtn')
let avg = document.getElementById('averageBtn')
let display = document.getElementById('display')

add.addEventListener('click', function() {
    let addNum = document.createElement('input')
    addNum.type = 'number'
    addNum.classList.add('num')
    nums.appendChild(addNum)

    let delNum = document.createElement('button')
    delNum.innerText = 'x'
    delNum.addEventListener('click', function() {
        addNum.remove()
        delNum.remove()
    })
    nums.appendChild(delNum)
})

avg.addEventListener('click', function() {
    let sum = 0
    for (let i=0; i < num.length; i++) {
        sum += parseFloat(num[i].value)
    }
    let average = sum/num.length
    let p = document.createElement('p')
    p.innerText = `Your average is: ${parseFloat(average).toFixed(2)}`
    display.prepend(p)
})