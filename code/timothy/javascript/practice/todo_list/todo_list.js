// an array to hold todo list items
let todoItems = []

function renderTodo(todo) {
    // Select the first element with a class of `js-todo-list`
    const list = document.querySelector('.js-todo-list');
  
    // Use the ternary operator to check if `todo.checked` is true
    // if so, assign 'done' to `isChecked`. Otherwise, assign an empty string
    const isChecked = todo.checked ? 'done': '';
    // Create an `li` element and assign it to `node`
    const node = document.createElement("li");
    // Set the class attribute
    node.setAttribute('class', `todo-item ${isChecked}`);
    // Set the data-key attribute to the id of the todo
    node.setAttribute('data-key', todo.id);
    // Set the contents of the `li` element created above
    node.innerHTML = `
      <input id="${todo.id}" type="checkbox"/>
      <label for="${todo.id}" class="tick js-tick"></label>
      <span>${todo.text}</span>
      <button class="delete-todo js-delete-todo">
      <svg><use href="#delete-icon"></use></svg>
      </button>
    `;
  
    // Append the element to the DOM as the last child of
    // the element referenced by the `list` variable
    list.append(node);
}

// a function to create new todos from text via the input
// pushed to our array
function addTodo(text) {
    const todo = {
        text, //set to the function arg
        checked: false, // initialized to false
        id: Date.now(), // id is created as number of milliseconds elapsed since Jan 1 1970, aka always unique
    }
    todoList.push(todo) // pushes new todo object to our array
    console.log(todoList) //logs todolist array in console
}

// selecting the form element
const form = document.querySelector('.jsform')
// adding a submit event listener
form.addEventListener('submit', event => {
    // preventing the page refreshing on form submission
    event.preventDefault()
    // selecting the text input
    const input = document.querySelector('.js-todo-input')
    // getting the value of the input and removing whitespace
    const text = input.value.trim()
    if (text !== '') {
        addTodo(text) // runs our addTodo func and pushes new item to array
        input.value = '' // resets the form to an empty string
        input.focus() // keeps the input selected after submission for multiple adds
    }
})



