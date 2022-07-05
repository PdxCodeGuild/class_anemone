new Vue({
    el: '#app',
    data: {
        tasks : [
            {text : 'Finish Lab 4'}
        ],
        inputField: "",
        completedTasks : []
    },
    methods: {
        addNewTask: function() {
            this.tasks.push({text: this.inputField})
        },
        removeTask: function(task) {
            this.tasks.splice(this.tasks.indexOf(task), 1)
        },
        completedTask: function(task) {
            this.completedTasks.push({text: task})
            this.tasks.splice(this.tasks.indexOf(task), 1)
        }
    }
})