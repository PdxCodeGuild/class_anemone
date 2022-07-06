let ds = new Vue({
    el:'#app',
    data: {
        todos: [
            {text:'groceries', complete:false},
            {text:'decorations', complete:false},
            {text:'speech', complete:false},
            {text:'texting', complete:false},
        ],
        newtodo: "",
    },
    
    methods: {
        addTodo: function() {
            this.todos.push({text: this.newtodo, complete:false})
        },
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        truefalsey: function(todo) {
            let status = this.todos[this.todos.indexOf(todo)]
            if (status.complete === false) {
                status.complete = true
            }   else {
                status.complete = false
            }
        }
    }
})