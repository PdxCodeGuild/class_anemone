var incompleteList = new Vue({
    el: '#incomplete-list',
    data: {
        todos: [
            {text: 'placeholder example 1 todo item'}
        ],

        inputField: "",
    },

    methods: {
        addTodo: function () {
            this.incompleteList.todos.push({text: this.inputField})
        },
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        completeTodo: function(todo) {
            this.completeList.todos.push({text: this.inputField})
            this.todos.splice(this.todos.indexOf(todo), 1)
            // change complete to true here
        }
    },

    
    computed: {
        complete: function() {
            // do a .filter here for complete: true
        },
        incomplete: function() {
            // do a .filer here for complete: true -- this is a javascript function
        }
    }
})

// var completeList = new Vue({
//     el: '#complete-list',
//     data: {
//         todos: [
//             {text: 'completed item 1 - example paceholder'}
//         ],
//     },

//     methods: {
//         removeTodo: function(todo) {
//             this.todos.splice(this.todos.indexOf(todo), 1)
//         },
//     }
// })