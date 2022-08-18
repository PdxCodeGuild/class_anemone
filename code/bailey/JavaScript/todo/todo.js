let addItem = document.getElementById("addItem")
let addBtn = document.getElementById("addBtn")
let todoDiv = document.getElementById("todo")
let completeDiv = document.getElementById("complete")

addBtn.addEventListener('click', function(){

    let resultDiv = document.createElement('div')
    let resultP = document.createElement('p')
    let removeItem = document.createElement('button')
    let toggleItem = document.createElement('button')
    let complete = false

    removeItem.innerText='Remove'
    toggleItem.innerText='Mark Complete'

    
    resultP.innerText = addItem.value
    resultDiv.appendChild(removeItem)
    resultDiv.appendChild(toggleItem)
    resultDiv.appendChild(resultP)

    removeItem.addEventListener('click', function(){
        resultDiv.remove()
    })

    toggleItem.addEventListener('click', function(){

        if(complete === false){
            completeDiv.prepend(resultDiv)
            toggleItem.innerText='Mark Incomplete'
            complete = true
        }else if(complete === true){
            todoDiv.prepend(resultDiv)
            toggleItem.innerText = 'Mark Complete'
            complete = false
        }
    })

    todoDiv.prepend(resultDiv)

})