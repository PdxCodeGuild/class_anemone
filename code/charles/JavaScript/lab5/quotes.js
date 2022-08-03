Vue.component('updown', {
    emits: ['update:page'],
    data: function() {
        return {
        page:1
        }
    },
    template:`
        <div>
            <button @click="nextq">Next Quote</button>
            <button @click="previousq">Previous Quote</button>
        </div>
    `,
    methods: {
        nextq: function() {
            this.page++
            this.$emit('nextq')
            console.log(this.page)
        },
        previousq: function() {
            if (this.page > 1) {
                this.page-- 
             }
            this.$emit('previousq')
            console.log(this.page)
        }
    }
})
  

const vm = new Vue({
    el:"#quote",
    data: {
        quotd: {},
        quotes: {},
        error: {},
        typesearch: '',
        input:'',
        input1: '',
        input2: '',
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
        loadquota: function()  {
            if (this.typesearch === 'author') {
                axios({
                    method: 'get', 
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        type: this.typesearch,
                        filter: (this.input1+'+'+this.input2)
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
            } 
        },
        loadquott: function()  {
            if (this.typesearch === 'tags') {
                axios({
                    method: 'get', 
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        type: this.typesearch,
                        filter: this.input,
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
            } 
        },
        loadquotu: function()  {
            if (this.typesearch === 'user') {
                axios({
                    method: 'get', 
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        type: this.typesearch,
                        filter: this.input,
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
            } 
        },
        nextq: function() {
            this.page++
            if (this.typesearch === 'author') {
                axios({
                    method: 'get', 
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        type: this.typesearch,
                        filter: (this.input1+'+'+this.input2),
                        page:this.page
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
            } 
            if (this.typesearch === 'tags') {
                axios({
                    method: 'get', 
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        type: this.typesearch,
                        filter: this.input,
                        page:this.page
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
            }
            if (this.typesearch === 'user') {
                axios({
                    method:'get',
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        type: this.typesearch,
                        filter: this.input,
                        page:this.page
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
            }
        },
        previousq: function() {
            if (this.page > 1) {
               this.page-- 
            }  console.log(this.page)          
            if (this.typesearch === 'author') {
                axios({
                    method: 'get', 
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        type: this.typesearch,
                        filter: (this.input1+'+'+this.input2),
                        page:this.page
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
            } 
            if (this.typesearch === 'tags') {
                axios({
                    method: 'get', 
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        type: this.typesearch,
                        filter: this.input,
                        page:this.page
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
            }
            if (this.typesearch === 'user') {
                axios({
                    method:'get',
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        type: this.typesearch,
                        filter: this.input,
                        page:this.page
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
            }
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
                this.quotes = response.data
                console.log(this.quotes, response.data)
            }).catch(error => {
                console.log(error, error.response.data)
                this.error = error.response.data
        })
    }
})
