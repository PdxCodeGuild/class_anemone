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
        location: '',
        // user enters gps cordinates, zip or city and state
        // need results sorted by closest first
        // can later allow user to choose sort function
        pageNumber: 1,
        // the starting page number
        // equivalent to current_page in the json data
        userBreed: '',
        breedList: [
            {breed: 'akita', activites: ['hiking', 'hunting', 'skiing'], endurance: false}, // tested
            {breed: 'alaskan malamute', activites: ['hiking', 'running', 'skiing'], endurance: true}, //tested
            {breed: 'american eskimo dog', activites: ['hiking'], endurance: false}, // tested
            {breed: 'american staffordshire terrier', activites: ['hiking'], endurance: false}, // tested
            // {breed: 'anatolian shephard', activites: ['hiking', 'running'], endurance: true}, // tested not working
            // {breed: 'australian cattle dog', activites: ['hiking', 'running'], endurance: true}, // tested not working
            {breed: 'australian kelpie', activites: ['hiking', 'running'], endurance: true}, // tested
            // {breed: 'australian shephard', activites: ['hiking', 'running'], endurance: true}, // tested not working
            {breed: 'labrador retriever', activities: ['hiking', 'hunting'], endurance: false}, 
            {breed: 'husky', activites: ['hiking', 'running', 'skiing'], endurance: true}, // tested
            {breed: 'golden retriever', activites: ['hiking', 'hunting'], endurance: false}, // tested

            // activites SPELLED WRONG NEED TO CHANGE ALL INSTANCES OF IT
    ]
        // endurance is not currently used but is added as something to be used in future
        // it can be an option for individuals such as marathon runners looking for dogs that can go the distance
        // given to dog breeds with extreme potential for athletic ability ONLY of course individual dogs will vary

        // ranking system -- > hiking -- considered on a more casual level (day hiker level)
                          // running -- more intense energy level than hiking
                          // hunting -- dog breeds that were designed for hunting
                                    // potential future categories -- retrieval, pointers, sight hounds, scent hounds
                          // skiing -- all the classic sled dog breeds + some other long haired breeds like akita
                                    // later add a 'mushing/pulling' for only the sled dog breeds?
                /// can also go through and look at pets listed under each breed to get a since of which breeds are more inclined for the 
                /// endurance attribute as most are mixes so the breeds are somewhat subjective
                /// also when ENDURANCE option checked senior dogs should be excluded from results
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