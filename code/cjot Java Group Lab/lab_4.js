// let delta = document.getElementById('delete')
// let omega = document.getElementById('create')
// let mark = document.getElementById('completed')
let nitems = document.getElementsByClassName('nitem')
let itemDiv = document.getElementById('todoitem')
let Confirm = document.getElementById('submit')
let completedDiv = document.getElementById('completeditems')

Confirm.addEventListener('click', function() {
    let addeditem = document.querySelector('input').value
    let resultP = document.createElement('p')
    resultP.innerText=addeditem

    let itemRemove = document.createElement('button')
    itemRemove.innerText = '×'
    itemRemove.addEventListener('click', function(){
        resultP.remove()
        itemRemove.remove()
    })
    
    let itemComplete = document.createElement('button')
    itemComplete.innerText = '✓'
    itemComplete.addEventListener('click', function(){
        resultP.remove()
        itemRemove.remove()
        itemComplete.remove()
    })
    
    completedDiv.appendChild(resultP)
    itemDiv.appendChild(itemComplete)
    itemDiv.appendChild(resultP)
    itemDiv.appendChild(itemRemove)

    
})

// Confirm.addEventListener('click', function() {
    
// })
