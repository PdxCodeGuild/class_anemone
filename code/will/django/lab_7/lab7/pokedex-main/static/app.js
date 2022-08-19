Vue.component('pokemon-item', {
    data: function() {
        return {
            editMode: false
        }
    },
    props: ['item'],
    template: `
        <div>
            <div v-if="editMode">
                <input type="text" v-model="item.name">
                <input type="text" v-model="item.height">
                <input type="text" v-model="item.weight">
                <input type="text" v-model="item.image_front">
                <input type="text" v-model="item.image_back">
                <button @click="savePokemon(item)">Save</button>
              
            </div>
            <div v-else>
                <p>{{ item.number }}</p>
                <p>{{ item.name }}</p>
                <img :src="item.image_front">
                <img :src="item.image_back">
                <p>height: {{ item.height }}</p>
                <p>weight: {{ item.weight }}</p>
                <br>
                <button @click="editMode=true">Edit</button>
                <button @click="removePokemon(item)">Remove Pokemon</button>
            </div>  
        </div>
    `,
    methods: {
        savePokemon: function(item) {
            this.$emit('save', item)
            this.editMode = false
        },
        removePokemon: function(item) {
            this.$emit('remove', item)
        }
    }
})

const vm = new Vue({
    el: "#app",
    delimiters: ['[[',']]'],
    data: {
        csrfToken: "",
        pokemon: [],
        newPokemon: {
            "number": "",
            "name": "",
            "height": "",
            "weight": "",
            "image_front": "",
            "image_back": "",
            "caught_by":[],
        },
        users:[],
        currentUser:{},
        currentUserID:'',
        thisPokemon : {
            "number": 166,
            "name": "bulbasaur",
            "height": 0.7,
            "weight": 6.9,
            "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
            "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png",
            "caught_by": [3]
        }
    },
    methods: {
        loadPokemon: function() {
            axios({
                method: 'get',
                url: 'api/v1/'
            }).then(response => {
                this.pokemon = response.data
                console.log(response.data)
            }).catch(error => {
                console.log(error)
                console.log(error.response_data)
            })
        },
        createPokemon: function() {
            axios({
                method: 'post',
                url: 'api/v1/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: {
                    "number": this.newPokemon.number,
                    "name": this.newPokemon.name,
                    "height": this.newPokemon.height,
                    "weight": this.newPokemon.weight,
                    "image_front": this.newPokemon.image_front,
                    "image_back": this.newPokemon.image_back,
                    "caught_by": [this.currentUserID]
                }
            }).then(response => {
                this.loadPokemon()
                this.newPokemon = {
                    "number": "",
                    "name": "",
                    "height": "",
                    "weight": "",
                    "image_front": "",
                    "image_back": "",
                    "caught_by": "",
                }
            })
        },
        savePokemon: function(item) {
            axios({
                method: 'patch',
                url: `api/v1/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: item
            }).then(response => {
     
            })
        },
        removePokemon: function(item) {
            axios({
                method: 'delete',
                url: `/api/v1/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: item
            }).then(response => {
                this.loadPokemon()
            })
        },
        loadCurrentUser: function() {
            axios({
                method:'get',
                url:'api/v1/current-user/',
                headers:{
                    'X-CSRFToken': this.csrfToken
                }
            }).then(response=> {
                this.currentUser = response.data
                this.currentUserID = this.currentUser.id
                console.log('The current user: ', this.currentUser)
                // console.log(this.currentUser['id'])

                console.log(this.currentUserID)
            })
        }
    },
    created: function() {
        this.loadPokemon()
        this.loadCurrentUser()
    },
    mounted: function() {
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})