const vm = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
        csrfToken: "",
        pokemons: [],
        types: [],
        edit: false,
        createdPokemon: {
            "number": null,
            "name": "",
            "height": null,
            "weight": null,
            "image_front": "",
            "image_back": "",
        }
    },
    
    props: ['pokemon'],

    methods:{
        loadPokemon: function(){
            axios({
                method: 'get',
                url: '/api/pokemon/'
            }).then(response => {
                this.pokemons = response.data
                console.log(response.data)
            })
        },
        loadTypes: function(){
            axios({
                method: 'get',
                url: '/api/types/'
            }).then(response => {
                this.types = response.data
            })
        },
        hidePokemon: function(){
            this.pokemons = []
        },
        createPokemon: function() {
            axios({
                method: 'post',
                url: '/api/pokemon/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: this.createdPokemon
            }).then(response => {
                this.loadPokemon()
                this.createdPokemon = {
                    "number": null,
                    "name": "",
                    "height": null,
                    "weight": null,
                    "image_front": "",
                    "image_back": "",
                }
            })
        },
        savePokemon: function(pokemon) {
            axios({
                method: 'patch',
                url: `api/pokemon/${pokemon.id}/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: pokemon
            }).then(response => {
                this.loadPokemon()
            })
        },
        removePokemon: function(pokemon) {
            axios({
                method: 'delete',
                url: `api/pokemon/${pokemon.id}/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                }
            }).then(response => {
                this.loadPokemon()
            })
        },
        editPokemon: function() {
            this.edit = !this.edit
            console.log(this.edit)
        }
        
    }, 






    created: function() {
        this.loadTypes()
    },

    mounted: function() {
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }


})