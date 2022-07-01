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
    // let itemcom = document.createElement('p')
    // itemcom.
    resultP.innerText=addeditem

    let itemRemove = document.createElement('button')
    itemRemove.innerText = '×'
    itemRemove.addEventListener('click', function(){
        resultP.remove()
        itemRemove.remove()
        itemComplete.remove()
    })
    
    let undo = true
    let itemComplete = document.createElement('button')
    itemComplete.innerText = '✓'
    itemComplete.addEventListener('click', function() {
        if (undo === true) {
            resultP.style.textDecoration = "line-through"
            completedDiv.appendChild(resultP)
            completedDiv.appendChild(itemComplete)
            completedDiv.appendChild(itemRemove)
            undo = !undo
        } else {
            resultP.style.textDecoration ='none'
            itemDiv.appendChild(resultP)
            itemDiv.appendChild(itemComplete)
            itemDiv.appendChild(itemRemove)
            undo = !undo
        }
        // resultP.remove()
        // itemRemove.remove()
        // itemComplete.remove()
        // completedDiv.appendChild(resultP)
        // completedDiv.appendChild(itemComplete)
        // completedDiv.appendChild(itemRemove)
    })

   
    
    // completedDiv.appendChild(resultP)
    
    itemDiv.appendChild(resultP)
    itemDiv.appendChild(itemComplete)
    itemDiv.appendChild(itemRemove)

    
})

// Confirm.addEventListener('click', function() {
    
// })
