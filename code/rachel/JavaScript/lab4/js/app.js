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
        // completedTask: function(task) {
        //     let compTask = this.tasks.splice(this.tasks.indexOf(task), 1)
        //     this.completedTasks.push({text: compTask})
            
        // }
    },
    computed: {
        completedTask() {
            
        }
    }
})