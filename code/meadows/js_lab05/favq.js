
const vm = new Vue({
    el:"#app",
    data: {
        authors: {},
        selected: null,
        inputTxt: null,
        page: 1,
    },
    
    methods: {
        loadRando: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => {
                this.authors = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        loadSearch: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qoutes',
                params: {
                    type: this.selected,
                    filter: this.inputTxt,
                    page: this.page
                },
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => {
                this.authors = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        previousPage: function() {
            this.page --
            this.loadSearch()
        },
        nextPage: function() {
            this.page ++
            this.loadSearch()
        }
    },
    created: function() {
        axios({
            method:'get',
            url: 'https://favqs.com/api/quotes/',
            headers: {
                "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
            }
            }).then(response => {
                this.authors = response.data
                console.log(this.quotes, response.data)
            }).catch(error => {
                console.log(error, error.response.data)
                this.error = error.response.data})
    }
})