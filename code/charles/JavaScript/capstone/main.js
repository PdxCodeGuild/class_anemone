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
        ainput:''
    },
    
    methods:{
        
        qsearch: function() {
            
            axios({
                method: 'get',
                url: 'http://openlibrary.org/search.json',
                params: {
                    q: this.qinput,
                    limit:10
                }
            }).then(response => {this.qout = response.data})
            
            .catch(error => {
                console.log(error, error.response.data)
                this.error=error.response.data})
                
        },
        
        tsearch: function() {
            axios({
                method: 'get',
                url: 'http://openlibrary.org/search.json',
                params:{
                    title: this.tinput,
                    limit: 10
                }
            }).then(response => {this.tout = response.data})
            .catch(error => {
                console.log(error, error.response.data)
                this.error=error.response.data})
        },
        
        asearch: function() {
            axios({
                method: 'get',
                url: 'http://openlibrary.org/search.json',
                params:{
                    author: this.ainput,
                    limit:10
                }
            }).then(response => {this.aout = response.data})
            .catch(error => {
                console.log(error, error.response.data)
                this.error=error.response.data})
        },
        
    },
    // computed: {
    //     isquotloaded() {
    //         const nestedLoaded = Object.keys(this.quot).map(key => this.quot[key].length !==0)
    //         return this.qout && nestedLoaded.length !== 0
    //     }
    // }
})