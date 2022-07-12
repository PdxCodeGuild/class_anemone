const vm = new Vue({
    el:"#main",
    data:{
        response:{},
        out:{},
        sout:{},
        error:{},
        element:'',
        element2: '',
        element3:''
    },

    methods:{
        loadhome: function() {
            axios({
                method: 'get',
                url: 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service'
            }).then(response => {this.out = response.json}, console.log(response.data, this.out))
            .catch(error => {
                console.log(error, error.response.data)
                this.error=error.response.data})
        },
        search: function() {
            if (element2 != '') {
                element +='/'+element2
            } if (element3 != '') {
                element +='/'+element3
            }
            axios({
                method: 'get',
                url: 'https//www.dnd5eapi.com/api/'+this.element
            }).then(response => {this.sout = response.data},
            console.log(response.data)).catch(error => {this.error=error.response.data})
        }
    }
})