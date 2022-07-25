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
                <button @click="savePokemon(item)">Save</button>
            </div>
            <div v-else>
                <p>{{ item.number }}</p>
                <p><strong>{{ item.name }}</strong></p>
                <img :src="item.image_front">
                <p><em>-height: {{ item.height }}</em></p>
                <p><em>-weight: {{ item.weight }}</em></p>
                <p><em>-type:</em></p>
                <ul>
                    <li v-for="type in item.type_info">
                        <p><em>{{ type.type }}</em></p>
                    </li>
                </ul>
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
        types: [],
        newPokemon: {
            "number": null,
            "name": "",
            "height": null,
            "weight": null,
            "image_front": "",
            "image_back": "",
            "type": ""
        },
    },
    methods: {
        loadPokemon: function() {
            // this.pokemon = {}
            axios({
                method: 'get',
                url: 'api/v1/pokemon/'
            }).then(response => {
                this.pokemon = response.data
                console.log(response.data)
            }).catch(error => {
                console.log(error)
                console.log(error.response_data)
            })
        },
        loadTypes: function() {
            axios({
                method: 'get',
                url: 'api/v1/types/'
            }).then(response => {
                this.types = response.data
                console.log(response.data)
            }).catch(error => {
                console.log(error)
                console.log(error.response_data)
            })
        },
        createPokemon: function() {
            axios({
                method: 'post',
                url: 'api/v1/pokemon/',
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: this.newPokemon
            }).then(response => {
                this.loadPokemon()
                this.newPokemon = {
                    "number": null,
                    "name": "",
                    "height": null,
                    "weight": null,
                    "image_front": "",
                    "image_back": "",
                    "type": ""
                }
            })
        },
        savePokemon: function(item) {
            axios({
                method: 'patch',
                url: `api/v1/pokemon/${item.id}/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: item
            }).then(response => {
                this.loadPokemon()
            })
        },
        removePokemon: function(item) {
            axios({
                method: 'delete',
                url: `api/v1/pokemon/${item.id}/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                }
            }).then(response => {
                this.loadPokemon()
            })
        }
    },
    created: function() {
        this.loadPokemon()
        this.loadTypes()
    },
    mounted: function() {
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})