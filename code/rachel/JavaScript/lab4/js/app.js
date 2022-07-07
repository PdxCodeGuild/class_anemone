new Vue({
    el: '#app',
    data: {
        tasks : [],
        inputField: "",
    },
    methods: {
        addNewTask: function() {
            this.tasks.push({text: this.inputField, completed : false})
            this.inputField = ''
        },
        removeTask: function(task) {
            this.tasks.splice(this.tasks.indexOf(task), 1)
        },
        markTask: function(task) {
            if (task.completed === true) {
                task.completed = false
            } else {
                task.completed = true
            }
        },
    },
    computed: {
        completedTask: function() {
            return this.tasks.filter(function(item){
                return item.completed === true
            })
        },
        incompleteTask: function() {
            return this.tasks.filter(function(item){
                return item.completed === false
            })
        }
    }
})