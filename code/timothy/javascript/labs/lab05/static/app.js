Vue.component('pagination', {
    props: ['page'],
    template: `
        <div>
            <button @click="nextPage">Next Page</button>
        </div>
    `,
    data: function() {
        return {
            nextpage: this.page
        }
    },
    methods: {
        nextPage: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.searchText,
                    type: this.searchTag,
                    page: this.page,
                    last_page: this.last_page
                },
                headers: {
                    "Authorization": `Token token="3599aff7e790f1c38ab2e9ee892e36bf"`,}
            })
            this.nextpage++
            this.$emit('next-page', this.nextpage)
            console.log(this.nextpage)
        }
    }
})


const vm = new Vue({
    el: "#app",
    data: {
        ranQuotes: {},
        searchQuotes: {},
        searchText: "",
        searchTag: "",
        page: 1,
        
    },
    methods: {
        loadRanQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="3599aff7e790f1c38ab2e9ee892e36bf"`
                }
            }).then(response => {
                this.ranQuotes = response.data
            }).catch(error => {
                console.log(error)
                console.log(error.response.data)
            })
        },
        search: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.searchText,
                    type: this.searchTag,
                    page: this.page,
                    last_page: this.last_page
                },
                headers: {
                    "Authorization": `Token token="3599aff7e790f1c38ab2e9ee892e36bf"`}

            }).then(response => this.searchQuotes = response.data)
            .then(console.log(this.searchQuotes))
            .catch(error => {
                console.log(error)
                console.log(error.response.data)
            })
        }
    },
    created: function() {
        this.loadRanQuotes()
    }
})