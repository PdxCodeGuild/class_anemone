let vm = new Vue({
  el: '#content',
  data: {
    qotd: {}
  },
  methods: {
    loadQuote: function() {
        axios({
          method: 'get',
          url: 'https://favqs.com/api/qotd'
        }).then(response => this.qotd = response.data)
        .catch(error => {
            console.log(error)
            console.log(error.response.data)
        })
        }
    },
  created: function() {
    this.loadQuote()
  }
})
