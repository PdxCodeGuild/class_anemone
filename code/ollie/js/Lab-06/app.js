let numLetters = document.getElementById('num-letters')
let playGame = document.getElementById('play-game')
let rules = document.getElementById('rules')
let wordDiv = document.getElementById('word-div')
let guesses = document.getElementById('guess-div')
let guessBtn = document.getElementById('guess-btn"')

// Alert game rules and controls when RULES is selected
rules.addEventListener('click', function() {
    alert("Welcome to Hangman! Select how many letters you would like to be in your mystery word. Hit PLAY whenever you're ready and the game shall begin. Five wrong guesses and it's game over. Good luck!")
})

// Grab random word from API when PLAY is selected
playGame.addEventListener('click', function() {
    wordDiv.innerHTML = '{{ info }}'
})

playGame.addEventListener('click', function() {
    new Vue({
        el: '#word-div',
        data () {
            return {
                info: null
            }
        },
        mounted () {
            axios
            .get('https://random-word-api.herokuapp.com/word', {params: {length: parseInt(numLetters.value)}})
            .then(response => (this.info = response.data[0]))
        }
    })
})

function addLetter() {
    document.querySelector('#guessed-letters').innerHTML += (document.querySelector('#letter-input')).value
}