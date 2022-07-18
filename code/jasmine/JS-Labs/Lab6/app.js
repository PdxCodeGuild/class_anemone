

// Vue.component('movie-object', {
 
//     props: ['movie', 'addToWatchLater', 'isInWatchLater', 'removeWatchLater'],

//     template: `
//     <div class="card">
//     <img class="card-img-top" :src="movie.Poster" :alt="movie.Title">
//     <div class="card-body">
//       <h5 class="card-title">{{movie.Title}}</h5>
//       <p class="card-text">{{movie.Year}}</p>
//       <button
//       v-if="addToWatchLater && !isInWatchLater(movie)"
//       @click="addToWatchLater(movie)"
//       type="button"
//       class="btn btn-success">Watch Later</button>
//       <button
//         v-if="removeWatchLater"
//         @click="removeWatchLater(movie)"
//         type="button"
//         class="btn btn-danger">Remove</button>
//     </div>
//   </div>
//     `
// })

const API_URL = 'http://www.omdbapi.com/?apikey=b97ab39d&?type=movie&s=$';
const vm= new Vue({
    el: '#app',
    data : {
      searchTerm:'',
      results:[],
      error: '',
      watchLater:[],

    },
    methods:{
      async getResults() {
        const url = `${API_URL}${this.searchTerm}`;
        const response = await fetch(url);
        const data = await response.json();
        if (data.Error) {
          this.results = [];
          this.error = data.Error;
        } else {
          this.results = data.Search;
          this.error = '';
        }
      },
      addToWatchLater(movie) {
        this.watchLater.push(movie);
      },
      removeWatchLater(movie) {
        const index = this.watchLater.indexOf(movie);
        this.watchLater.splice(index, 1);
      },
      isInWatchLater(movie) {
        return this.watchLater.some(wl => wl.imdbID === movie.imdbID);
      },
    },
  })
