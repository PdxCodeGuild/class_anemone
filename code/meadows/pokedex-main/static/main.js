const vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        csrfToken: "",
        pokemon: [],
        users: [],
        currentUser: {},  
    },
    methods: {
        loadPokemon: function() {
            axios({
                method: 'get',
                url: '/apis/v1/pokemon/',
            }).then(response => this.pokemon = response.data)
        },
        loadUsers: function() {
            axios({
                method: 'get',
                url: '/apis/v1/users/',
            }).then(response => this.users = response.data)
        },
        loadCurrentUser: function() {
            axios({
                method: 'get',
                url: '/apis/v1/currentuser/',
            }).then(response => this.currentUser = response.data)
        },
        catchPokemon: function(poke) {
            this.currentUser.caught.push(poke.id)
            axios({
                method: 'patch',
                url: '/apis/v1/currentuser/',
                headers: {
                    'X-CSRFToken': this.csrfToken,
                },
                data: {
                    "caught": this.currentUser.caught
                }
            }).then(response => {
                this.loadCurrentUser()
            })
        },
        releasePokemon: function(poke) {
            console.log(poke.id)
            this.currentUser.caught.splice(this.currentUser.caught.indexOf(poke.id), 1)
            axios ({
                method: 'patch',
                url: '/apis/v1/currentuser/',
                headers: {
                    'X-CSRFToken': this.csrfToken,
                },
                data: {
                    "caught": this.currentUser.caught
                }
            }).then(response => {
                this.loadCurrentUser()
            })
        }
    },
    created: function() {
        this.loadPokemon()
        this.loadUsers()
        this.loadCurrentUser()
    },
    mounted: function() {
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }

})