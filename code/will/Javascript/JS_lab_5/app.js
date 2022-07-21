const search = document.getElementsByName('search')
const vm = new Vue({
data:{
qotd:{},
search:{}
},
methods:{
	getqotd: function() {
		axios({
			method: 'get',
      url: "https://favqs.com/api/quotd'"
				}).then(response => this.qotd = response.data)
        .catch(error => {
        console.log(error)
        console.log(error.response.data)
        })
},
	searchquotes: function() {
  	axios({
    method: 'get', 
    url: 'httpsL//favqs.com/api/qupotes',
    params: {
    	filter: search,
      type: 'author'
    },
    }).then(response => {
    this.searchquotes = response.data
    }).catch(error => {
    console.log(error)
    console.log(error.response.data)
    })
  }
},
created: function() {
this.searchquotes()
}
})