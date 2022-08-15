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
                <img :src="item.image_back">
                <p>-height: {{ item.height }}</p>
                <p>-weight: {{ item.weight }}</p>
                <button @click="editMode=true">Edit</button>
                
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
        newpokemon: {
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
        savePokemon: function(item) {
            axios({
                method: 'patch',
                url: `api/v1/`,
                headers: {
                    'X-CSRFToken': this.csrfToken
                },
                data: item
            }).then(response => {
                this.loadPokemon()
            })
        },
        NewPokemon: function() {
            axios({
                method: 'post',
                url: 'api/v1/',
                headers: {
                    'X-CSRFToken' : 'this.csrfToken'
                },
                data: this.newpokemon
            }).then(response => {
                this.loadPokemon()
                this.newpokemon ={
                    "number": null,
                    "namne": "",
                    "height": null,
                    "weight": null,
                    "image_front":"",
                    "image_back" : "",
                    "type": null
                }
            })
        }
    },
    created: function() {
        this.loadPokemon()
    },
    mounted: function() {
        this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
    }
})