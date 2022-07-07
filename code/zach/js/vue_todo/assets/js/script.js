let vm = new Vue({
  el: '#app',
  data: {      
    todos: [
      { text: 'Push Me' },
      { text: 'And Just Touch Me' },
      { text: 'Till I get my' },
      { text: 'Satisfaction' },
    ],
    inputField: '',
    return: {
      isIncomplete: false,
      isFinished: true,    
    } 

  },
  methods: {
    addTodo: function () {
      this.todos.push({ text: this.inputField });
    },
    delTodo: function (todo) {
      // console.log(todo)
      this.todos.splice(this.todos.indexOf(todo), 1);
    },
    findClass: function () {
      return this.class;
    },
    markDone: function (event) {
      console.log(this.class);
      if (this.class == 'col btn btn-outline-success btn-sm') {
        this.class = 'col btn btn-success btn-sm';
      } else {
        this.class = 'col btn btn-outline-success btn-sm';
      }
    },
  },
});
