new VTTCue({
    el: '#app',
    data: {

    },
    methods: {

    },
    mounted() {
        // get data from favqs.com
        axios({
            method: 'get',
            url: 'https://favqs.com/api/qotd'
        }).then((response) => {
            console.log(response.data)
        })
    }
})