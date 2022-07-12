const vm = new Vue ({
    el: '#app',
    data: {
        queryData: {},
        moonAge: "",
        today: "",
        
    },
    methods: {
        moonMapper: function() {
            axios({
                method: 'get',
                url: 'api.meteomatics.com',
                params: {
                    user: "pdxcodeguild_johnson",
                    validdatetime: "",
                    location: [45.5202471, -122.674194],
                    parameter: "moon_age:d",
                    format: 'json',
                }
            }).then( response => {
                this.queryData = response.data[0]
                console.log(this.queryData)

            })
        }
    }
})