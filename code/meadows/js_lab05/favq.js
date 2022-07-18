const vm = new VTTCue({
    el:"#app",
    data: {
        rando: {},
        searched: {},
        inputTxt: "",
        inputTag: "",
        page: 1,
    },
    
    methods: {
        loadRando: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => {
                this.rando = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        }
    }
})