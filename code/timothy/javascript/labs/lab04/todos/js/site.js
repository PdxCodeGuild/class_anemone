new Vue ({
    el: '#app',
    data: {
        newTodo: "",
        todos: [
            { text: 'Learn Vue' },
        ],
        completeTodos: [
            { text: 'Eat sushi' },
        ],
        isComplete: false,
    },
    methods: {
        createTodo: function() {
            this.todos.push({text: this.newTodo})
        },
        deleteTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        deleteComplete: function(complete) {
            this.completeTodos.splice(this.todos.indexOf(complete), 1)
        },
        completeTodo: function(todo) {
            newComplete = this.todos.splice(this.todos.indexOf(todo), 1)
            this.completeTodos.push({text: this.todo})
        }

    }
})