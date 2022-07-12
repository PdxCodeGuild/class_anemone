// var pf = new petfinder.Client({apiKey: "QUQDsRiiouriGF02BN27GLhwZWufM4PSoAxwGypLyH9WjTtpS7", secret: "Yoe36Ouy6oVLiXlX7hJCQJMkDW5VJHhxDLQ73LEw"});
// console.log(pf)
// dogData = {}
// pf.animalData.type('Dog')
//     .then(function (response) {
//     dogData = response.data
//     })
// console.log(dogData)

// import { Client } from "@petfinder/petfinder-js";

// dogData = {}

// const client = new Client({
//   apiKey: "QUQDsRiiouriGF02BN27GLhwZWufM4PSoAxwGypLyH9WjTtpS7",
//   secret: "Yoe36Ouy6oVLiXlX7hJCQJMkDW5VJHhxDLQ73LEw",
//   token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJRVVFEc1JpaW91cmlHRjAyQk4yN0dMaHdaV3VmTTRQU29BeHdHeXBMeUg5V2pUdHBTNyIsImp0aSI6ImYwNTM0YzA3NzQxMGNkYWEzNTc4OTBhNmFhYWNjN2E1NmEyZmNiMzM1MTY3OWRjM2U0ZjQ1NWZkOGFlNmVhZGFhNGNhNDYyOTFiMGIyOTk0IiwiaWF0IjoxNjU3NTgxMTk0LCJuYmYiOjE2NTc1ODExOTQsImV4cCI6MTY1NzU4NDc5NCwic3ViIjoiIiwic2NvcGVzIjpbXX0.xjgzg6GVNSyF-xFmzgADul54dZoz54-_ceHl8KuE9GWpcmO6x7svILSFrS6rNu-dLCcrPeJ99qdRukWPJ209QSbd9iP59YPjTfRbxjBKwxa4vxFPiW3Wv0UPzW9KEoeuAqdtEseE23-qz0_K17Ez7Bro2_JlC4rScQ6j-PEdEnsrvH0wTbgmlciHAvtJmPg-pNQ1SEvQJXmwgnvuUfQdZ_QXO7srS3PaAKz7JiJPBzz-Y8hoGvHTcJ5kamuK6sx0MRmmmLA6fj11AODQ2tyjGFYklPh3xUhbsayp6COiKADu8LpmC7wTlFptEPgTyokB_mqsMLE4UgI0J0SKw42AOQ",
// });

// client.animalData.breeds('dog')
//   .then(resp => {
//     dogData = resp.data.breeds
//     console.log(dogData)
//   });

// import { Client } from "@petfinder/petfinder-js";
// Client = require('@petfinder/petfinder-js');

// pf: new petfinder.Client({apiKey: "QUQDsRiiouriGF02BN27GLhwZWufM4PSoAxwGypLyH9WjTtpS7", secret: "Yoe36Ouy6oVLiXlX7hJCQJMkDW5VJHhxDLQ73LEw"})

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
        hikingBreeds: {},
        runningBreeds: {},
        cyclingBreeds: {},
        huntingBreeds: {}
        // list out all the breeds that fall into each category
        // can add 'endurance' key with true or false to each breed as well
    },
    methods: {

        getDogData: function() {
            pf.animal.search().then(function (response) {
                this.dogData = response.data
                console.log(response)
            }).catch(function(error) {
                console.log(error)
            })
       },
        // getDogData: function() {
        //     axios({
        //         method: 'get',
        //         url: 'https://api.petfinder.com/v2/',
        //         headers: {
        //             "Authorization": `Token token="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJRVVFEc1JpaW91cmlHRjAyQk4yN0dMaHdaV3VmTTRQU29BeHdHeXBMeUg5V2pUdHBTNyIsImp0aSI6ImYwNTM0YzA3NzQxMGNkYWEzNTc4OTBhNmFhYWNjN2E1NmEyZmNiMzM1MTY3OWRjM2U0ZjQ1NWZkOGFlNmVhZGFhNGNhNDYyOTFiMGIyOTk0IiwiaWF0IjoxNjU3NTgxMTk0LCJuYmYiOjE2NTc1ODExOTQsImV4cCI6MTY1NzU4NDc5NCwic3ViIjoiIiwic2NvcGVzIjpbXX0.xjgzg6GVNSyF-xFmzgADul54dZoz54-_ceHl8KuE9GWpcmO6x7svILSFrS6rNu-dLCcrPeJ99qdRukWPJ209QSbd9iP59YPjTfRbxjBKwxa4vxFPiW3Wv0UPzW9KEoeuAqdtEseE23-qz0_K17Ez7Bro2_JlC4rScQ6j-PEdEnsrvH0wTbgmlciHAvtJmPg-pNQ1SEvQJXmwgnvuUfQdZ_QXO7srS3PaAKz7JiJPBzz-Y8hoGvHTcJ5kamuK6sx0MRmmmLA6fj11AODQ2tyjGFYklPh3xUhbsayp6COiKADu8LpmC7wTlFptEPgTyokB_mqsMLE4UgI0J0SKw42AOQ"`
        //         }
        //     }).then(response => {
        //         this.dogData = response.data
        //         console.log(response)
        //         console.log(dogData)
        //     })
        // },

    created: function() {
        this.getDogData()
    }
    }
})