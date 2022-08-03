// JS Lab 4 Todos

const vm = new Vue({
    el: '#task',
    data: {
        tasks: [
            {id: 1, text: "Clean the kitchen", completed: false},
            {id: 2, text: "Wash the car", completed: false},
            {id: 3, text: "Feed the cat", completed: false}
        ], 
        newTaskText: "",
        newTaskId: 4,
    },
    computed: {
        notComplete: function() {
            return this.tasks.filter(function(task) {
                return !task.completed
            })
        },
        isComplete: function() {
            return this.tasks.filter(function(task) {
                return task.completed 
            })
        }
    },
    methods: {
        addTask: function() {
            this.tasks.push({id: this.newTaskId, text: this.newTaskText, completed: false})
            this.newTaskId++
            this.newTaskText = ""
        },
        removeTask: function(task) {
            this.tasks.splice(this.tasks.indexOf(task), 1)
        },
        toggleTask: function(task) {
            task.completed = !task.completed
        }
    }
})