let to_do_list = []

let user_input = document.getElementById("to_do_list");
let add_button = document.getElementById("to_do_button");
let itemsDiv = document.getElementById("items-div")


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
    })

    itemsDiv.appendChild(removeItem)

})

