const vm = new Vue({
    el: "#app",

    data: {
        books: [],
        characters: {},
        ring: {},
        Two: {},
        Three: {},
        Four: {},
        Five: {},
        Six: {},
        Seven: {},
        Eight: {},
        Nine: {},
        Ten: {},
        Eleven: {},
        Twelve: {},
        Thirteen: {},
    },

    methods: {

        loadAnime: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/',
            }).then((response) => {
                this.characters=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadOne: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/black_clover',
            }).then((response) => {
                this.ring=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadTwo: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/bleach',
            }).then((response) => {
                this.Two=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadThree: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/dragon_ball',
            }).then((response) => {
                this.Three=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadFour: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/jujutsu_kaisen',
            }).then((response) => {
                this.Four=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadFive: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/fma_brotherhood',
            }).then((response) => {
                this.Five=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadSix: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/naruto',
            }).then((response) => {
                this.Six=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadSeven: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/gintama',
            }).then((response) => {
                this.Seven=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadEight: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/itachi_uchiha',
            }).then((response) => {
                this.Eight=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadNine: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/one_piece',
            }).then((response) => {
                this.Nine=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadTen: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/demon_slayer',
            }).then((response) => {
                this.Ten=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadEleven: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/attack_on_titan',
            }).then((response) => {
                this.Eleven=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadTwelve: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/hunter_x_hunter',
            }).then((response) => {
                this.Twelve=response.data
            }).catch(error => console.log(error.response.data))
        },
        loadThirteen: function() {
            axios({
                method: 'get',
                url: 'https://anime-facts-rest-api.herokuapp.com/api/v1/boku_no_hero_academia',
            }).then((response) => {
                this.Thirteen=response.data
            }).catch(error => console.log(error.response.data))
        },
    },
    created: function() {
        this.loadAnime()
        // this.loadFact()
    }
})

//4011664222391367

// const vm = new Vue({
//     el: "#app",

//     components: {
//         //
//     },

//     mounted: function () {
//         axios.get('https://anime-facts-rest-api.herokuapp.com/api/v1/')
//             .then(response => console.log(response))
//             // .then(response => this.posts = response.data)
//             // .catch(error => this.post = [{title: "No post found"}])
//             // .finally(() => console.log('data loading complete.'))
//     },

//     data: {
//         posts:null,
//     }
// })
  
  
  
