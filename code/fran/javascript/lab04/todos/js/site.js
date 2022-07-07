let vm = new Vue({
    el: '#app',
    data: {
        todos: [],
        inputField: "",
      },
    methods: {
    addTodo: function() {
        this.todos.push({text: this.inputField})
    },
    removeTodo: function(todo) {
        // console.log(todo)
        this.todos.splice(this.todos.indexOf(todo), 1)
    }
    }
})