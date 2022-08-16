var task = document.getElementById('task_input')
var todo = document.getElementById('todo')
var addTask = document.getElementById('add-task')
var done = document.getElementById('done')


addTask.addEventListener('click', function(){
    var show_task = document.createElement('div')
    var new_task = document.createElement('p')

    var deleteTask = document.createElement('button')
    deleteTask.innerText = 'x'
    deleteTask.addEventListener('click', function(){
        show_task.remove()
    })

    let state = true
    let toggle = document.createElement('button')
    toggle.innerText = 'Complete'
    new_task.innerText = task.value 
    show_task.appendChild(new_task)
    show_task.appendChild(deleteTask)
    show_task.appendChild(toggle)
    toggle.addEventListener('click', function(){
        if (state == false) {
            new_task.setAttribute('style', 'text-decoration:none')
            todo.prepend(show_task)
            state=true
        }

        else{
            new_task.setAttribute('style', 'text-decoration: line-through')
            done.prepend(show_task)
            state=false
        }
    })

    new_task.innerText = task.value 
    todo.prepend(show_task)
})
