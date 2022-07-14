// console.log("hello World")

const form = document.querySelector('form');
const input = document.querySelector('#searchTerm')
const resultsSection = document.querySelector('#results')
const watchLaterSection = document.querySelector('#results')

const API_URL = 'http://www.omdbapi.com/?apikey=b97ab39d&?type=movie&s=';

form.addEventListener('submit', formSubmitted);

async function formSubmitted(event) {
    event.preventDefault();
    // console.log('form submitted');
    const searchTerm = input.value;
    try {
        const results = await getResults(searchTerm)
        showResults(results);
    }   catch(error) {
        showError(error)
    }
    // console.log(searchTerm)
}

async function getResults(searchTerm){
    const url = `${API_URL}${searchTerm}`;
    // console.log(url);
    const response = await fetch(url);
    const data = await response.json();
    if(data.Error) {
        throw new Error(data.Error);
    }
    return data.Search;
        
}



function showResults(results){
    resultsSection.innerHTML = results.reduce((html, movie) => {
        return html + getMovieTemplate(movie, 4);
    }, '');

    const watchLaterButtons = document.querySelectorAll('.watch-later-button');
    watchLaterButtons.forEach(button => {
        button.addEventListener('click', (event) =>{
            const { id } = button.dataset; 
            const movie = results.find(movie => movie.imdbID === id);
            watchLaterSection.innerHTML = watchLaterSection.innerHTML + getMovieTemplate(movie,1,false)
            // console.log(movie)
        });
    });
}

function getMovieTemplate(movie, cols, button = true) {
    return `
    <div class="card col-${cols}">
    <img class="card-img-top" src="${movie.Poster} alt="${movie.Ttile}">
    <div class="card-body">
      <h5 class="card-title">${movie.Title}</h5>
      <p class="card-text">${movie.Year}</p>
      ${button ? ` <button data-id="${movie.imdbID}" type="button" class="btn btn-primary watch-later-button">Watch Later</a>
      `
      : ''
}
    </div>
  </div>`
}

function showError(error){
    resultsSection.innerHTML = `<div class="alert alert-danger" role="alert">
    ${error.message}
  </div>`
}