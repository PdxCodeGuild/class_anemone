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
        imageSrc: "",
        songKeys: [],
        citySongData: {},
        portlandChart: "ip-city-chart-5746545",
        portlandList: {},
        portlandTracks: []

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
                this.imageSrc = this.tracks[0].track.images.background
                console.log(this.tracks[0].track)
                this.artist = this.tracks[0].track.subtitle
                console.log(this.tracks.track)
                
                
            }).catch(error => {
                console.log(error)
                console.log(error.response.data)
            })
        },
        songDetail: function() {
            axios({
                method: 'get',
                url: 'https://shazam.p.rapidapi.com/songs/get-details',
                params: {
                    
                }
            })
        },
        citySongs: function() {
            axios({
                method: 'get',
                url: 'https://shazam.p.rapidapi.com/charts/list',
                headers: {
                    'X-RapidAPI-Key': '75ce0b8eb6mshfbcf000a06cbf85p128692jsnf4792066f2d7',
                    'X-RapidAPI-Host': 'shazam.p.rapidapi.com'
                }
            }).then(response => {
                this.citySongData = response.data
                console.log(this.citySongData.countries[10].cities[32])

            }).catch(error => {
                console.log(error)
                console.log(error.response.data)
            })
        },
        portlandSongChart: function() {
            axios({
                method: 'get',
                url: 'https://shazam.p.rapidapi.com/charts/track',
                headers: {
                    'X-RapidAPI-Key': '75ce0b8eb6mshfbcf000a06cbf85p128692jsnf4792066f2d7',
                    'X-RapidAPI-Host': 'shazam.p.rapidapi.com'
                },
                params: {
                    locale: "en-US",
                    listId: "ip-city-chart-5746545",
                    pageSize: 10
                }
            }).then(response => {
                this.portlandList = response.data
                console.log(this.portlandList)
                this.portlandTracks = this.portlandList.tracks
                console.log(this.portlandTracks)
            })
        }
    },
    created: function() {
        this.citySongs()
        this.portlandSongChart()
    }

})