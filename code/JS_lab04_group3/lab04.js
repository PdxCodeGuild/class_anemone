let item = document.getElementById('item_input')
let todo_div = document.getElementById('todo')
let addItemBtn = document.getElementById('add-item')
let complete = document.getElementById('complete')

addItemBtn.addEventListener('click', function() {
   
   
    
    let result_div = document.createElement('div')
    let resultP = document.createElement('p')
    

    let itemRemove = document.createElement('button')
    itemRemove.innerText = '×'
    itemRemove.addEventListener('click', function() {
       result_div.remove()
    })
    let state = true
    let toggle = document.createElement('button')
    toggle.innerText = 'toggle'
    resultP.innerText = item.value
    result_div.appendChild(resultP)
    result_div.appendChild(itemRemove)
    result_div.appendChild(toggle) 
    toggle.addEventListener('click', function(){
        if (state === false){
            resultP.setAttribute('style', 'text-decoration: none')
            todo_div.prepend(result_div)
            state=true

        }
        else{
            resultP.setAttribute('style', 'text-decoration: line-through')
            complete.prepend(result_div)
            state=false
        }
    })
    resultP.innerText = item.value
    todo_div.prepend(result_div)

})