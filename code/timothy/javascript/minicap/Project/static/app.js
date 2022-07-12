const app = new Vue ({
    el: '#app',
    data: {
        message: "Vue-tiful",
        searchCharacter: "",
        character: {},
        apikey: "53f4a537d556878664a50b0e1f08997eda83778d",
        publcKey: "d663c33e04f65f27501d3d51fb0dff12",
        timestamp: Date.now(),
        hash: ""
    },
    methods: {
        createHash: function() {
            timestamp = timestamp
        },
        loadCharacter: function() {
            axios({
                method: 'get',
                url: "http(s)://gateway.marvel.com/v1/public/characters",
                params: {
                    name: this.searchCharacter,
                    apikey: "53f4a537d556878664a50b0e1f08997eda83778d",
                    publcKey: "d663c33e04f65f27501d3d51fb0dff12",
                },

            }).then(response => {
                this.character = response.data
                console.log(this.character)
            }).catch(error => {
                console.log(error)
                console.log(error.response.data)
            })
        }
    }
})