const vm = new Vue({
    el: "#app",
    data: {
        searchString: "",
        startYear: null,
        endYear: null,
        result: {}
    },
    methods: {
        loadResult: function() {
            this.result = {}
            axios({
                method: 'get',
                url: 'https://images-api.nasa.gov/search',
                params: {
                    description: this.searchString, 
                    media_type: 'image',
                    year_start: this.startYear,
                    year_end: this.endYear
                }
            }).then(response => {
                this.result = response.data
                console.log(response.data)
            }).catch(error => {
                console.log(error)
                console.log(error.response_data)
            })
        }
    }
})