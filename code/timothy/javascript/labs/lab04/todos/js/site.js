new Vue ({
    el: '#app',
    data: {
        newTodo: "",
        todos: [
            { text: 'Learn Vue', isComplete: false },
            { text: 'Eat sushi', isComplete: true },
        ],
    },
    methods: {
        createTodo: function() {
            this.todos.push({text: this.newTodo, isComplete: false})
        },
        deleteTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        completeTodo: function(dex) {
            this.todos[dex].isComplete = true
        },
        incompleteTodo: function(dex) {
            this.todos[dex].isComplete = false
        }

    },
    computed: {
        incompleteList() {
            return this.todos.filter(todo => ! todo.isComplete)
        },
        completeList() {
            return this.todos.filter(todo => todo.isComplete)
        }
    }
})