const vm = new Vue ({
    el: '#app',
    data: {
        searchResults: {},
        searchResultName: "",
        searchResultTitle: "",
        searchTerm: "",
        searchType: ""
    },
    methods: {
        loadResults: function() {
            axios({
                method: 'get',
                url: 'https://api.lyrics.ovh/v1/',
                params: {
                    artist: this.searchResultName,
                    title: this.searchResultTitle
                }
                
            }).then(response => this.searchResultName = response.data)
            .then(console.log(this.searchResultName)
            .catch(error => {
                console.log(error)
                console.log(error.response.data)
            })
        )}
    }
})