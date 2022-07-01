let todoInput = document.querySelector('#todo-text');
let todoForm = document.querySelector('#todo-form');
let todoList = document.querySelector('#todo-list');
let completeList = document.querySelector('#complete-list');
let todoCount = document.querySelector('#todo-count');

let todos = [];
let complete = [];

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

let renderComplete = () => {
  completeList.innerHTML = '';
  for (let i = 0; i < complete.length; i++) {
    let item = complete[i];

    let li = document.createElement('li');
    li.textContent = item;
    li.setAttribute('complete-index', i);

    let completeBtn = document.createElement('button');
    completeBtn.textContent = 'Incomplete';
    let deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    li.appendChild(completeBtn);
    li.appendChild(deleteBtn);
    completeList.appendChild(li);
  }
};

todoForm.addEventListener('submit', (event) => {
  event.preventDefault();

  let todoText = todoInput.value.trim();

  todos.push(todoText);
  todoInput.value = '';
  console.log('click', todoText);

  renderTodo();
});

todoList.addEventListener('click', (event) => {
  let element = event.target;

  if (element.matches('button') === true) {
    let command = element.textContent;

    switch (command) {
      case 'Delete':
        index = element.parentElement.getAttribute('todo-index');
        todos.splice(index, 1);
        renderTodo();
        break;
      case 'Complete':
        console.log(command, 'case');
        index = element.parentElement.getAttribute('todo-index');
        let slice = todos.splice(index, 1);
        complete.push(slice);
        renderTodo();
        renderComplete();
        break;
      default:
        console.log('default');
        break;
    }
  }
});

completeList.addEventListener('click', (event) => {
  let element = event.target;

  if (element.matches('button') === true) {
    let command = element.textContent;

    switch (command) {
      case 'Delete':
        index = element.parentElement.getAttribute('complete-index');
        complete.splice(index, 1);
        renderComplete();
        break;
      case 'Incomplete':
        console.log(command, 'case');
        index = element.parentElement.getAttribute('complete-index');
        let slice = complete.splice(index, 1);
        todos.push(slice);
        renderTodo();
        renderComplete();
        break;
      default:
        console.log('default');
        break;
    }
  }
});

let init = () => {
  renderTodo();
};

init();
