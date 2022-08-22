Vue.component('quotes-result', {
    props: ['componentquote'],  // componentQuote represents a single quote from the api response
    template: `
        <li>
            <p>{{ componentquote.body }}</p>
            <p><em>- {{ componentquote.author }}</em></p>
            <br>
        </li>
    `
})

const vm = new Vue({
    el: "#app",
    data: {
        searchString: null,
        selectedType: null,
        requestedPage: 1,
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
                // this.quotesResult = null
                // console.log(response)
                this.quotesResult = response.data
                console.log(response.data)
            }).catch(error => {
                console.log(error)
                console.log(error.response_data)
            })
        },
        previousPage: function() {
            this.requestedPage --
            this.loadSearchQuotes()
        },
        nextPage: function() {
            this.requestedPage ++
            this.loadSearchQuotes()
        }
    },
    created: function() {
        this.loadSearchQuotes()
    }
})
