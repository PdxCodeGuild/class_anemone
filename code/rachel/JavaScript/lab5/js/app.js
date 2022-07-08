Vue.component('quote-list', {
    props: ['quote'],
    template:
    `<li>
        {{ quote.body }}<br>
        -{{ quote.author }}<br><br>
    </li>`
})

new Vue({
    el: '#app',
    data: {
        qotd: {},
        inputField: "",
        typeSelect: "",
        requestedQuotes: {},
        page: 1,
    },
    methods: {
        loadQotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    Authorization: `Token token="09ada82d2e12eed2b8ec418f90bcd028"`
                }
            }).then((response) => {
                this.qotd = response.data
            })
        },
        loadRequestedQuotes: function() {
            // get data from favqs.com
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.inputField,
                    type: this.typeSelect,
                    page: this.page,
                },
                headers: {
                    Authorization: `Token token="09ada82d2e12eed2b8ec418f90bcd028"`
                }
            }).then((response) => {
                this.requestedQuotes = response.data
            })
        },
        // nextPage: function() {

        // }
    },
    created: function() {
        this.loadQotd()
    }
})