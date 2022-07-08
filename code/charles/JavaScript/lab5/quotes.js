Vue.component('next', {
    data:{
        page: 2
    },
    template:`
        <div>
            <button @click="nextq">Next Quote</button>
        <div>
    `,
    methods: {
        nextq: function() {
            this.$emit('next', {page:this.page})
            this.page++
        }
    }
})

Vue.component('previous', {
    data: {
        page: 2
    },    
    template:`
        <div>
            <button @click="previousq">Previous Quote</button>
        <div>
    `,
    methods: {
        previousq: function() {
            this.$emit('next', {page:this.page})
            this.page--
        }
    }
})

const vm = new Vue({
    el:"#quote",
    data: {
        quotd: {},
        quotes: {},
        error: {},
        first: '',
        last:'',
        page:1
    },
    methods: {
        loadquotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd'
            }).then(response => this.quotd = response.data)
            .catch(error => {
                console.log(error, error.response.data)
                this.error = error.response.data
            })
        },
        loadquots: function()  {
            axios({
                method: 'get', 
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: (this.first+'+'+this.last),
                    type: 'author',
                    page: page
                },
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => {
                this.quotes = response.data
                console.log(this.quotes, response.data)
            }).catch(error => {
                console.log(error, error.response.data)
                this.error = error.response.data
            })
        },
        // searching: function() {
        //     for (i=0,i<search.length,i++) {
        //         if (i === ' ') {this.search += '+'} 
        //         else {this.search += i}
        //     }
        // }
    }
})