// JS Lab 4 Todos

const vm = new Vue({
    el: '#quotes',
    data: {
        todos: [
            {id: 1, text: "Clean the kitchen", completed: false},
            {id: 2, text: "Wash the car", completed: false},
            {id: 3, text: "Feed the cat", completed: false}
        ], 
        newTodoText: "",
        newTodoId: 4,
    },
    computed: {
        notComplete: function() {
            return this.todos.filter(function(todo) {
                return !todo.completed
            })
        },
        isComplete: function() {
            return this.todos.filter(function(todo) {
                return todo.completed 
            })
        }
    },
    methods: {
        addTask: function() {
            this.todos.push({id: this.newTodoId, text: this.newTodoText, completed: false})
            this.newTodoId++
            this.newTodoText = ""
        },
        removeTask: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        toggleTask: function(todo) {
            todo.completed = !todo.completed
        }
    }
})