// Vue.component('load', {
//     data: function() {
//         return {
//             any: {}
//         }
//     },
//     template:`
//         <div>
//             <button @click="load">Load all Returned</button>
//         </div>
//         `,
//         methods: {
//             load: function() {

//             }
//         }
// })


const vm = new Vue({
    el:"#main",
    data: {
        standby:{},
        qout:{},
        tout:{},
        aout:{},
        error:{},
        qinput:'',
        tinput: '',
        ainput:'',
        limit:10,
    },
    
    methods:{
        
        qsearch: function() {
            this.quot = {}
            this.tout = {}
            this.aout = {}
            axios({
                method: 'get',
                url: 'http://openlibrary.org/search.json',
                params: {
                    q: this.qinput,
                    limit:  this.limit
                }
            }).then(response => {this.qout = response.data})
            
            .catch(error => {
                console.log(error, error.response.data)
                this.error=error.response.data})
                this.qinput = ''
                
        },
        
        tsearch: function() {
            this.quot = {}
            this.tout = {}
            this.aout = {}
            axios({
                method: 'get',
                url: 'http://openlibrary.org/search.json',
                params:{
                    title: this.tinput,
                    limit: this.limit
                }
            }).then(response => {this.tout = response.data})
            .catch(error => {
                console.log(error, error.response.data)
                this.error=error.response.data})
                this.tinput = ''
        },
        
        asearch: function() {
            this.quot = {}
            this.tout = {}
            this.aout = {}
            axios({
                method: 'get',
                url: 'http://openlibrary.org/search.json',
                params:{
                    author: this.ainput,
                    limit:  this.limit
                }
            }).then(response => {this.aout = response.data})
            .catch(error => {
                console.log(error, error.response.data)
                this.error=error.response.data})
                this.ainput = ''
        },
        
    },
    // computed: {
    //     isquotloaded() {
    //         const nestedLoaded = Object.keys(this.quot).map(key => this.quot[key].length !==0)
    //         return this.qout && nestedLoaded.length !== 0
    //     }
    // }
})