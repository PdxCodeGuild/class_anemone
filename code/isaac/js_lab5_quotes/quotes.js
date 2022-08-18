Vue.component('qotd-display', {
    template: `<h2>Quote of the Day</h2>`,
})

const vm = new Vue({
    el: '#app',
    data: {
        qotd: {},
        listQuotes: {},
        searchType: "",
        searchTag: "",
        reqPage: 1
    },
    methods: {
        loadQotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd'
            }).then(response => this.qotd = response.data)
            .catch(error => { 
                console.log(error)
                console.log(error.response.data)
            })
        },
        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.searchType,
                    type: this.searchTag,
                    page: this.reqPage
                },
                headers: {
                    "Authorization": `Token token="cda8804982a486346d86371faa09cae7"`
                }
            }).then(response => this.listQuotes = response.data) 
            .then(console.log(this.listQuotes)) 
            .catch(error => {
                console.log(error)
                console.log(error.response.data)
            })
        },
        backPage: function() {
            this.reqPage--
            this.loadQuotes()
        },
        nextPage: function() {
            this.reqPage++
            this.loadQuotes()
        }
    },
    created: function() {
        this.loadQotd()
    }
})
        