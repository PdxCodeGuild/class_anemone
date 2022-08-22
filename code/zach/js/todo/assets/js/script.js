let todoInput = document.querySelector('#todo-text');
let todoForm = document.querySelector('#todo-form');
let todoList = document.querySelector('#todo-list');
let todoCount = document.querySelector('#todo-count');

let todos = [];

let renderTodos = () => {
  todoList.innerHTML = '';
  todoCount.textContent = todos.length;

  // Create a list element for every todo in todos
  for (let i = 0; i < todos.length; i++) {
    let todo = todos[i];

    let li = document.createElement('li');
    li.textContent = todo;
    li.setAttribute('todo-index', i);

    let completeBtn = document.createElement('button');
    completeBtn.textContent = 'Complete';

    let deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';


    li.appendChild(completeBtn);
    li.appendChild(deleteBtn);
    todoList.appendChild(li);
  }
};

// save todos to local storage to prevent them from deleting upon refresh
let storeTodos = () => {
  localStorage.setItem('todos', JSON.stringify(todos));
}

todoForm.addEventListener('submit', (event) => {
  event.preventDefault();

  let todoText = todoInput.value.trim();

  todos.push(todoText);
  todoInput.value = '';
  console.log('click',todoText)

  renderTodos();
  storeTodos();
});

todoList.addEventListener('click', (event) => {
  let element = event.target;
  
  if (element.matches('button')=== true){
    let command = element.textContent
    switch(command){
      case 'Delete':
        console.log(command, 'case');
        break;
      case 'Complete':
        console.log(command, 'case');
        break;
      default:
        console.log('default');
        break;
    }
  }
})


function init () {
  let savedTodos = JSON.parse(localStorage.getItem('todos'))

  if (storeTodos !== null){
    todos = savedTodos || [];
  }
  renderTodos()
}

init()