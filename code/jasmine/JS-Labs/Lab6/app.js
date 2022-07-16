

// Vue.component('Movie', {
//     data: function () {
//         return {
//             clicks: 0
//         }
//     },
//     props: ['movie', 'addToWatchLater', 'isInWatchLater', 'removeWatchLater'],
//     template: `
//     <div class="card">
//     <img class="card-img-top" :src="movie.Poster" :alt="movie.Title">
//     <div class="card-body">
//       <h5 class="card-title">{{movie.Title}}</h5>
//       <p class="card-text">{{movie.Year}}</p>
//       <button
//         v-if="addToWatchLater && !isInWatchLater(movie)"
//         @click="addToWatchLater(movie)"
//         type="button"
//         class="btn btn-success">Watch Later</button>
//       <button
//         v-if="removeWatchLater"
//         @click="removeWatchLater(movie)"
//         type="button"
//         class="btn btn-danger">Remove</button>
//     </div>
//   </div>
//     `
// })

const API_URL = 'http://www.omdbapi.com/?i=tt3896198&apikey=b97ab39d';
const vm= new Vue({
    el: '#app',
    data : {
      searchTerm:'',
      results:[],
      error: '',

    },
    methods:{
      getResults : function (){
        this.result = {}
        this.error = '',
        axios({
          method: 'get',
          url : `http://www.omdbapi.com/?apikey=b97ab39d&?type=movie&s=${this.searchTerm}`,
       
        }).then(response => {
          this.results = response.data
          console.log(response.data)
        }).catch(error => {
          this.error = response.data
          console.log(error.response.data)
        })
    }
  }
});