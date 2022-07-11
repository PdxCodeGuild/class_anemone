var app = new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!'
    }
  })

  axios({
    method: 'get',
    url: 'https://api.funtranslations.com/translate/'
  }).then((response) => {
    console.log(response.data)
  })