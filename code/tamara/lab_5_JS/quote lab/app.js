Vue.component('user-search', {
    data: function() {
        return {
            userInput: '',
            userChoice: 'keyword',
        }
    },
    template:
        `<div>
            <input type="text" v-model="userInput" @keyup.enter="loadUserQuotes">
            <input type="radio" v-model="userChoice" value="keyword" id="keyword"><label for="keyword">keyword</label>
            <input type="radio" v-model="userChoice" value="tag" id="tag"><label for="tag">tag</label>
            <input type="radio" v-model="userChoice" value="author" id="author"><label for="author">author</label>
            <button @click="loadUserQuotes">Search</button>
        </div>`
    ,
    methods: {
        loadUserQuotes: function () {
            this.$emit('search', {userChoice: this.userChoice, userInput: this.userInput})
        },
    }
})

const quoteApp = new Vue ({
    el: '#quote-app',
    data: {
        randomQuotes: {},
        userQuotes: {},
        pageNumber: 1,
        lastUserInput: '',
        userInput: '',
        userChoice: 'keyword',
        lastUserChoice: '',
    },
    methods: {
        loadRandomQuotes: function () {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => this.randomQuotes = response.data)
        },

        loadUserQuotes: function (payLoad) {
            this.userInput=payLoad.userInput
            this.userChoice=payLoad.userChoice
            this.lastUserInput = this.userInput
            this.lastUserChoice = this.userChoice
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
                params: {
                    filter: this.lastUserInput,
                    type: this.lastUserChoice,
                    page: this.pageNumber,
                }
            }).then(response => {
                console.log(this.userInput)
                console.log(this.userChoice)
                this.userQuotes = response.data
            })
            
        },

        nextPage: function() {
            
            this.pageNumber ++

            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
                params: {
                    filter: this.lastUserInput,
                    type: this.lastUserChoice,
                    page: this.pageNumber,
                }
            }).then(response => {
                console.log(this.userInput)
                console.log(this.userChoice)
                console.log(this.pageNumber)
                this.userQuotes = response.data
            })
        },
        
        backPage: function() {
            
            this.pageNumber --
            
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
                params: {
                    filter: this.lastUserInput,
                    type: this.lastUserChoice,
                    page: this.pageNumber,
                }
            }).then(response => {
                console.log(this.userInput)
                console.log(this.userChoice)
                console.log(this.pageNumber)
                this.userQuotes = response.data
            })
        },
        
    },

    created: function () {
        this.loadRandomQuotes()
    }
}) 