const app = new Vue ({
    el: '#app',
    data: {
        trackSearchTerm: "",
        trackData: {}
    },
    methods: {
        trackSearch: function() {
            axios({
                method: 'get',
                url: 'https://api.musixmatch.com/ws/1.1/',
                params: {
                    q_track: this.trackSearchTerm,
                },
                headers: {
                    apikey: '31d3f66eca78f699be45e97edd21a6b7',
                    
                }
            }).then(response => {
                this.trackData = response.data
                console.log(this.trackData)
            })
        }
    }
})