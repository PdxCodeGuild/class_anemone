let items = document.getElementById('item_input')
let resultsDiv = document.getElementById('results')
let addItemBtn = document.getElementById('add-item')
let numDiv = document.getElementById('num-div')
// let addNumBtn = document.getElementById('add-num')

// Button to add another to-do item
// For each item, also include a Remove button and Complete button
// addNumBtn.addEventListener('click', function() {
//     let newNum = document.createElement('input')
//     newNum.type = 'number'
//     newNum.classList.add('num')

//     let newNumRemove = document.createElement('button')
//     newNumRemove.innerText = '×'
//     newNumRemove.addEventListener('click', function() {
//         newNum.remove()
//         newNumRemove.remove()
//     })

//     numDiv.appendChild(newNum)
//     numDiv.appendChild(newNumRemove)
// })

// Add each new item to the To Do list
addItemBtn.addEventListener('click', function() {
    let list = []

    list.push(items.value)

    // for (let i=0; i<nums.length;i++) {      // INSTEAD OF calculating, we add to list
    //     if (nums[i].value === "") {
    //         nums[i].value = 0
    //     }
    //     answer += parseFloat(nums[i].value)
    // }
    let resultP = document.createElement('p')
    resultP.innerText = list      // INSTEAD OF answer, we want to print list
    resultsDiv.prepend(resultP)
})