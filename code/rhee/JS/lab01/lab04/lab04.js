
  new Vue({
    el: '#app-5',
    data: {
      newTodo: '',
      existingTodo: [ 
        {text: "get items", 'id':1, 'completed':false, 'editing':false },
    ]
    },
    methods: {
      addTodo: function () {
        var text = this.newTodo.trim()
        if (text) {
          this.existingTodo.push({ text: this.newTodo, id: this.idForTodo, completed: false })
          this.newTodo = '';
          this.idForTodo++
        }
        },
        removeTodo(index) {
        this.existingTodo.splice(index, 1)
        },
        editTodo(todo) {
            // alert('Edit the text.')
        todo.editing = true
        },
        doneEdit(todo) {
        todo.editing = false
        },


      }

    }
)