let to_do_list = []
let completeList = []

let user_input = document.getElementById("to_do_list");
let add_button = document.getElementById("to_do_button");
let itemsDiv = document.getElementById("items-div")
let completeDiv = document.getElementById("completed-items")


add_button.addEventListener('click', function(){
    let item = user_input.value
    to_do_list.push(item)

    let printItem = document.createElement('p')
    printItem.innerText = item
    itemsDiv.prepend(printItem)

    let removeItem = document.createElement('button')
    removeItem.innerText = "Delete"
    removeItem.addEventListener('click', function(){
        printItem.remove()
        removeItem.remove()
        completeBtn.remove()
    })

    itemsDiv.appendChild(removeItem)

    let completeBtn = document.createElement('button')
    completeBtn.innerText = "Complete"
    completeBtn.addEventListener('click', function(){
        let completeItem = to_do_list.splice(to_do_list.indexOf(item), 1)
        console.log(completeItem)
        completeList.push(completeItem)
        console.log(completeList)
        removeItem.remove()
        completeBtn.remove()
        printItem.remove()
    })
    itemsDiv.appendChild(completeBtn)
    return item



})
// need to figure this out
