const vm = new Vue({
    el: "#app",
    data: {
        results: {},
    },
    methods: {
        notWorking: function() {
            axios({
                method: 'get',
                url: "https://api.vegancheck.me/v0/product ",
                headers: {
                    "AUTH-KEY": "alpha"
                }
            }).then((response) => {
                this.qotd = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
    },
    created: function() {
        this.notWorking()
    }
})

//4011664222391367
  
  
  
