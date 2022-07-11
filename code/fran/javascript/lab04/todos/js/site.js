// Lab04 - Vue Todos
// Fran Kappes

// 'add-todo' component that handles creating and adding an item to the to-do list
Vue.component('add-todo', {
    data: function() {
        return {
            text: "",       // initialize input field with an empty string
            id: 1           // first item added to to-do list will have an id of 1
        }
    },
    template: `
        <div>
            <input type="text" v-model="text" @keyup.enter="addTodo">
            <button v-on:click="addTodo">Add To List</button>
        </div>
    `,
    methods: {
        addTodo: function() {
            this.$emit('add', {id: this.id, text: this.text, completed:false})  // emits instruction for parent addTodo function to fire off
            this.id++       // incremement id to prepare for the next list item
            this.text = ""    // reset input field with an empty string 
        }
    }
})


// 'todo-item' component that displays both incomplete and completed to-do items
// Handles marking items as complete and incomplete
// Handles removal of list items
Vue.component('todo-item', {
    props: ['todo'],    // allows this component to "see" the parent todo dataset
    template: `
        <p>
            <input type="checkbox" v-model="todo.completed">
            <template>{{ todo.text }}</template>
            <button v-on:click="$emit('remove', todo)">×</button>
        </p>
    `,
    methods: {
        removeTodo: function(todo) {
            this.$emit('remove', todo)      // tells parent removeTodo function to fire off
        },
        toggleTodo: function(todo) {
            this.$emit('toggle', todo)      // changes complete status for an item
        }
    }
})

// Root component
const vm = new Vue ({
    el: "#app",
    data: {
        todos: []
    },
    computed: {
        incompleteTodos: function() {
            return this.todos.filter(function(todo) {
                return !todo.completed                  // return only incompleted todo items
            })
        },
        completeTodos: function() {
            return this.todos.filter(function(todo) {
                return todo.completed                   // return only completed todo items
            })  
        }
    },
    methods: {
        addTodo: function(todo) {
            this.todos.push(todo)               // adds new item to the todo list
        },
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)      // removes items from todo list
        },
        toggleTodo: function(todo) {
            todo.completed = !todo.completed        // changes 'completed' status for an item
        }
    }
})