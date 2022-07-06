var todosList = new Vue({
    el: '#lists-div',
    data: {
        todos: [
            {text: 'placeholder example 1 todo item', complete: false},
        ],

        inputField: "",
    },

    methods: {
        addTodo: function () {
            this.todos.push({text: this.inputField, complete: false})
            this.inputField= ''
        },

        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        completeTodo: function(todo) {
            todo.complete = true
        },

        undoComplete: function(todo) {
            todo.complete = false
        }
    },

    
    computed: {
        complete: function() {
            return this.todos.filter(function (element) {
                return (element.complete === true)
            })
        },

        incomplete: function() {
           return this.todos.filter(function (element) {
                return (element.complete === false)
           })
        }
    }
})