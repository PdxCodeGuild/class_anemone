let newItem =  document.getElementById("newItem")
let createButton = document.getElementById("createBtn")
let itemList = document.getElementById("itemList")
let completeList = document.getElementById("completeList")


let todos = []

createButton.addEventListener('click', function() {
    todo = {
        text,
        checked: false,
        id: Date.now(),
    }
    todos.push(todo)
    console.log(todos
})