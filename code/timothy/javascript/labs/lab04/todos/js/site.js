new Vue ({
    el: '#app',
    data: {
        newTodo: {
            text: '',
            isComplete: false,
            id: 0
        },
        todos: [
            
            
        ],
    },
    methods: {
        createTodo: function() {
            this.todos.push({text: this.newTodo.text, isComplete: this.newTodo.isComplete, id: this.newTodo.id})
            this.newTodo.id ++
            this.newTodo.text = ""
        },
        deleteTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        completeTodo: function(todo) {
            todo.isComplete = true
        },
        incompleteTodo: function(todo) {
            todo.isComplete = false
        }

    },
    computed: {
        incompleteList: function() {
            return this.todos.filter(todo => ! todo.isComplete)
        },
        completeList: function() {
            return this.todos.filter(todo => todo.isComplete)
        }
    }
})