const vm = new Vue({
    el: "#app",
    data: {
        searchString: null,
        selectedType: null,
        requestedPage: 2,
        quotesResult: {}
    },
    methods: {
        loadSearchQuotes: function() {
            // this.quotesResult = {}
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.searchString, 
                    type: this.selectedType,
                    page: this.requestedPage
                },
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => {
                this.quotesResult = null
                console.log(response)
                // console.log(response.data)
                this.quotesResult = response.data
            }).catch(error => {
                console.log(error)
                console.log(error.response_data)
            })
        }
    },
    created: function() {
        this.loadSearchQuotes()
    }
})
