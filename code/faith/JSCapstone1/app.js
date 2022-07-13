var app = new Vue({
    el: '#app',
    data: {
        message: '',
        url: 'https://api.funtranslations.com/translate/pig-latin.json',
        results: {},
        translated:''
    },
    methods: {
        getPigLatin: function() {
            axios({
                method: 'get',
                url: 'https://api.funtranslations.com/translate/pig-latin.json',
                params: {
                   
                    text:this.message
                }
                }
              ).then((response) => {
                console.log(response.data)
                this.results=response.data
                this.translated = this.results.contents.translated
              })
        }
        
    }
  })



  
  
//   axios({
//     method: 'post',
//     url: 'https://api.funtranslations.com/translate/pig-latin.json',
//     data: {
//         translated:this.message,
        
//     }
// }).then((response) => {
//     console.log(response.data)
// })
