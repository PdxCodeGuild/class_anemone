new Vue({
    el:'#app',
    data: {
        todos: [
            {text: 'Get BEER', complete: false},
            {text: 'Go Swimming with Sharks', complete: false},
            {text: 'Befriend a Grizzly Bear', complete: false}
        ],
        New: '',
    },
    
    methods: {
        addTodo: function() {
            this.todos.push({text: this.New, complete: false})
        },
        Remove: function(todo) {
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
    },
})