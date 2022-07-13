const dogFinder = new Vue ({
    el: '#dog-finder',
    data: {
        pf: new petfinder.Client({apiKey: "QUQDsRiiouriGF02BN27GLhwZWufM4PSoAxwGypLyH9WjTtpS7", secret: "Yoe36Ouy6oVLiXlX7hJCQJMkDW5VJHhxDLQ73LEw"}),
        dogData: {},
        // for storing the data returned by the api call of the different dogs
        activity: '',
        // activity will be selected by user via a checkbox
        // options == cycling, hiking, running, hunting
        // addition 'endurance' option for hardcore athletes
        // can add aditional options later and climate options like hot or cold climates
        // based on what the user selects it will filter by breed and it will only show adult and younger dogs
        location: '98294',
        // user enters gps cordinates, zip or city and state
        // need results sorted by closest first
        // can later allow user to choose sort function
        pageNumber: 1,
        // the starting page number
        // equivalent to current_page in the json data
        userBreed: '',
        breedList: [
            {breed: 'labrador retriever', activities: ['hiking', 'hunting'], endurance: false}, 
            {breed: 'husky', activites: ['hiking', 'running'], endurance: true},
            {breed: 'golden retriever', activites: ['running', 'hunting'], endurance: false},
    ]
        // can add 'endurance' key with true or false to each breed as well
    },
    methods: {

        getNewDogData: function() {
            this.pf.animal.search({
                type: "dog",
                breed: this.userBreed,
                page: this.pageNumber,
                location: this.location,
                // breed: "husky"
            }).then(response => {
                this.dogData = response.data
            })
            this.pageNumber = 1
        },
        
        getDogData: function() {
            this.pf.animal.search({
                type: "dog",
                breed: this.userBreed,
                page: this.pageNumber,
                location: this.location,
                // breed: "husky"
            }).then(response => {
                this.dogData = response.data
            })
       },

       nextPage: function() {
        this.pageNumber ++
        this.getDogData()
       },

       backPage: function() {
        this.pageNumber --
        this.getDogData()
       },

       activityType: function() {

       }

    // created: function() {
    //     this.getDogData()
    // }
    }
})