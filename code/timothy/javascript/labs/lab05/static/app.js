// Vue.component('search-quotes', {
//     data: function() {
//         return {
//             searchText: "",
//             searchTag: ""
// //         }
// //     },
//     template: `
//         <div>
//             <input type="text" placeholder="Search for quotes..." v-model="searchText">
//             <select name="terms" id="terms" v-model="searchTag">
//                 <option value="keyword" selected required>Keyword</option>
//                 <option value="author">Author</option>
//                 <option value="tag">Tag</option>
//             </select>
//             <button @click="search">Search</button>
//         </div>
//     `,
//     methods: {
//         search: function() {
//             axios({
//                 method: 'get',
//                 url: 'https://favqs.com/api/quotes',
//                 params: {
//                     filter: this.searchText,
//                     type: this.searchTag
//                 },
//                 headers: {
//                     "Authorization": `Token token="3599aff7e790f1c38ab2e9ee892e36bf"`}

//             }).then(response => this.searchQuotes = response.data)
//             .then(console.log(this.searchQuotes))
//             .catch(error => {
//                 console.log(error)
//                 console.log(error.response.data)
//             })
//         }
//     }
// })


const vm = new Vue({
    el: "#app",
    data: {
        ranQuotes: {},
        searchQuotes: {},
        searchText: "",
        searchTag: ""
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
                    type: this.searchTag
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