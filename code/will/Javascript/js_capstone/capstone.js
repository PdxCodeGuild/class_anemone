const vm = new Vue({
    el: "#app",
    data: {
        weather: {},
        temp_array: []
    },
    methods: {
        weather_get: function() {
            axios({
                method: 'get',
                url: 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=5237b4d3bbf26ec509a9bbf732d0e83a',
                params: {
                    appid : '5237b4d3bbf26ec509a9bbf732d0e83a',
                    lat : 45.7068,
                    lon : -121.5281,
                    units : 'imperial'
                    
                }
            }).then((response) => {
                this.weather = response.data
                this.temp_array = this.weather.list
                 console.log(response.data.temp)
                 })
                            },

        },     
    
    created: function() {
        this.weather_get()
        
    }
    
}) 

