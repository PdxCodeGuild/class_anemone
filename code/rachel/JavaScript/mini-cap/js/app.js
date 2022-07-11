new Vue({
    el: "#app",
    data: {
        recipes: {},
        inputField: "",
        mealTypeSelect: "",
        // healthLabelSelect: "",
        // cuisineTypeSelect: "",
    },
    methods: {
        loadSearchedRecipes: function() {
            axios({
                method: 'get',
                url: 'https://api.edamam.com/api/recipes/v2',
                params: {
                    type: 'any',
                    q: this.inputField,
                    app_key: '1a19da9ec31d6f8947067bda7bb211c7',
                    app_id: '0285e128',
                    mealType: this.mealTypeSelect,
                    // health: this.healthLabelSelect,
                    // cuisineType: this.cuisineTypeSelect,
                },
                header: {
                    'Accept': 'application/json'
                }
            }).then((response) => {
                this.recipes = response.data
            })
        }
    }
})