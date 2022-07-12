const vm = new Vue({
    el:"#main",
    data:{
        Chardata:{
            ability_scores:{},
            alignments:{},
            backgrounds:{},
            languages:{},
            proficiencies:{},
            skills:{}
        },
        Class:{

        },
        search:''
    },

    methods:{
        loadhome: function() {
            axios({
                method: 'get',
                url: 'https://www.dnd5eapi.co/api/ability-scores'
            }).then(response => this.quotd = response.data, console.log(response.data))
            .catch(error => {
                console.log(error, error.response.data)
                this.error=error.response.data})
        }
    }
})