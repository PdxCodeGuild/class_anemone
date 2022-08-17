new Vue({
    el: '#app',
    data: {
        todos: [],
        todoText:  " "
    },

    methods: {
        addTodo: function() {
            this.todos.push({text: this.todoText, completed: false})
        },

        removeTodo(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },

        toggleTodo(todo){
            todo.completed = !todo.completed

        }
    }

})