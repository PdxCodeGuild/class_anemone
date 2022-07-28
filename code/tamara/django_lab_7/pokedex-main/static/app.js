Vue.component('pokemon-item', {
    data: function() {
        return {
            editModeValue: false
        }
    },
    delimiters: ['[[', ']]'],
    props: ['pokemon'],
    template: 
        `<li>
            <div v-if="editModeValue">
                <input type="text" v-model="pokemon.name" placeholder="enter name">
                <input type="text" v-model="pokemon.front_image" placeholder="enter front image url">
                <input type="text" v-model="pokemon.back_image" placeholder="enter back image url">
                <input type="text" v-model="pokemon.height" placeholder="enter height">
                <input type="text" v-model="pokemon.weight" placeholder="enter weight">
            </div>

            <div v-else>
                <h3>[[ pokemon.name ]]</h3></div>
                <h4>Type(s):</h4>
                <h4 v-for="type in pokemon.type_detail">[[ type.type ]]</h4>
                <img :src="pokemon.image_front">
                <img :src="pokemon.image_back">
                <h4>height: [[ pokemon.height ]]</h4>
                <h4>weight: [[ pokemon.weight ]]</h4>
            </div>

            <div>
                <button @click="editModeValue = !editModeValue">Edit</button>
                <button @click="editPokemon(pokemon)">Complete</button>
                <button @click="deletePokemon(pokemon)">Delete</button>
            </div>
        
        </li>`
    ,

    methods: {
        deletePokemon: function(pokemon) {
            this.$emit('delete', pokemon)
        },
        editPokemon: function(pokemon) {
            this.$emit('edit', pokemon)
        }

    }
})

const vm = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        csrfToken: "",
        pokemon_list: [],
        editModeValue: false,
        // pokemon: {
        //     "name": '',
        //     "height": '',
        //     "weight": '',
        //     "image_front": '',
        //     "image_back": '',
        // },
        newPokemon: {
            "name": '',
            "number": '',
            "height": '',
            "weight": '',
            "image_front": '',
            "image_back": '',
            "caught_by": [],
        },
        users: [],
        },
    methods: {
        loadPokemon: function() {
            axios({
                method: 'get',
                url: '/api/v1/pokemon/'
            }).then(response => this.pokemon_list = response.data)
        },
        loadUsers: function() {
            axios({
                method: 'get',
                url: '/api/v1/users/'
            }).then(response => this.users = response.data)
        },
        createPokemon: function() {
            axios({
                method: 'post',
                url: '/api/v1/pokemon/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: this.newPokemon
                }).then(response => {
                    this.loadPokemon()
                    this.newPokemon = {
                        "name": '',
                        "number": '',
                        "height": '',
                        "weight": '',
                        "image_front": '',
                        "image_back": '',
                        "caught_by": [],
                    }
                })
        },
        editPokemon: function(pokemon) {
            axios({
                method: 'patch',
                url: `/api/v1/pokemon/${pokemon.id}/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: pokemon
            }).then(response => {
                this.loadPokemon()
                // this.pokemon = {
                //     "name": '',
                //     "height": '',
                //     "weight": '',
                //     "image_front": '',
                //     "image_back": '',
                // },
                this.editModeValue = false
            })
        },
        deletePokemon: function(pokemon) {
            axios({
                method: 'delete',
                url: `/api/v1/pokemon/${pokemon.id}/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
            }).then(response => {
                this.loadPokemon()
            })
        },
    },
    created: function() {
        this.loadPokemon()
        this.loadUsers()
    },
    mounted: function() {
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})