const vm = new Vue ({
    el: '#app',
    data: {
        searchTerm: "",
        searchResults: {},
        hits: {},
        hit: [],
        tracks: {},
        title: "",
        artist: "",

    },
    methods: {
        loadResults: function() {
            axios({
                method: 'get',
                url: 'https://shazam.p.rapidapi.com/search',
                params: {
                    term: this.searchTerm
                },
                headers: {
                    'X-RapidAPI-Key': '75ce0b8eb6mshfbcf000a06cbf85p128692jsnf4792066f2d7',
                    'X-RapidAPI-Host': 'shazam.p.rapidapi.com'
                }
            }).then(response => {
                this.searchResults = response.data
                this.hits = this.searchResults.tracks
                this.hit = this.hits.hits
                this.tracks = this.hit
                console.log(this.tracks)
                
            }).catch(error => {
                console.log(error)
                console.log(error.response.data)
            })
        }
    }
})