let to_do_list = []
let completeList = []

let user_input = document.getElementById("to_do_list");
let add_button = document.getElementById("to_do_button");
let itemsDiv = document.getElementById("items-div")
let completeDiv = document.getElementById("completed-items")
// let completeBtn = document.getElementById("complete")
// let removeItem = document.getElementById("delete")




add_button.addEventListener('click', function(){
    const item = user_input.value
    to_do_list.push(item)

    const printItem = document.createElement('p')
    printItem.innerText = item
    itemsDiv.prepend(printItem)

    itemsDiv.appendChild(printItem)
})

       
let buttonOne = completeBtn 

completeBtn.addEventListener('click', function(){
    completeBtn = document.createElement('button')
    completeBtn.innerText = "Complete"
    var completeItem = to_do_list.splice(to_do_list.indexOf(item), 1)
    completeList.push(completeItem)
    printItem.remove()
    removeItem.remove()
    completeBtn.remove()

    var displayItem = document.createElement('p')
    displayItem.classList.add("strike")
    displayItem.innerText = item
    completeDiv.prepend(displayItem) 
    
})   
itemsDiv.appendChild(completeBtn)

let buttonTwo = removeItem
removeItem.addEventListener('click', function(){
var removeItem = document.createElement('button')
removeItem.innerText = "Delete"
    printItem.remove()
    removeItem.remove()
    completeBtn.remove()
    
})
itemsDiv.appendChild(removeItem)

    
    
    
    
    
    
