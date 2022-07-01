let todoInput = document.querySelector('#todo-text');
let todoForm = document.querySelector('#todo-form');
let todoList = document.querySelector('#todo-list');
let todoCount = document.querySelector('#todo-count');

let todos = [];

function renderTodo() {
  todoList.innerHTML = '';
  todoCount.textContent = todos.length;

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
}

todoForm.addEventListener('submit', (event) => {
  event.preventDefault();

  let todoText = todoInput.value.trim();

  todos.push(todoText);
  todoInput.value = '';
  console.log('click', todoText)

  renderTodo();
})
let renderDelete = () => {
  console.log('delete')
}
let renderComplete = () => {
  console.log('delete');
};
todoList.addEventListener('click', (event) => {
  let element = event.target;

  if (element.matches('button') === true){
    let command = element.textContent;

    switch(command){
      case 'Delete':
        renderDelete();
        break;
      case 'Complete':
        renderComplete();
        break;
      default:
        break;
    }
  }
})

let init = () => {
  renderTodo();
}

init()