const App = {
        
    data() {
      return {
        notice: '',
        quotePrint: '',
        search: '',
        searchText:'',
        page: 1,
        lastPage: 'true',
        listStart: 1,

      }
    },
 
    methods: {

    getQuote (){
       axios({ 
        url: 'https://favqs.com/api/qotd',
        method: 'get'
    }).then(response => (this.quotePrint = response.data.quote.body))
    console.log(response)
  },


      
      searchQuotes () {
        axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        headers: { Authorization: `Token token="8f11f41caeb544443c9e3062693e97b1`},
        params: { filter: this.searchText , type: ""} 
      }).then(response => (this.search = response.data))
        console.log(search)

    },
   },
  }
  
  Vue.createApp(App).mount('#app')