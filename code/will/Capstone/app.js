
const vm = new Vue({
data:{
weather:{},
zillow:{}
},
methods:{
	getzillow: function() {
		axios({
			method: 'get',
      url: "http://www.zillow.com/webservice/ProReviews.htm?",
      params:{location: 'santa monica, ca', home_type: 'Houses'},
      headers:{
        'zwsid': 'X1-ZWz166nntaqn0r_aqadi',
        'email' : 'hotspam483@gmail.com',
        'output': 'json',
        }
    
       
				}).then(response => this.zillow = response.data)
        .catch(error => {
        console.log(error)
        console.log(error.response.data)
        })
},
	getweather: function() {
  	axios({
        method: 'GET',
        url: 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/historysummary?',
        params: {
        'key': 'TH8XVH87FPNHTEE3XWU2KQQPC',
        'chronoUnit':'years',
        'breakBy': 'years',
        'minYear':'1970',
        'maxYear' : '2022',
          longitude: '-118.4010845',
          latitude: '33.9463626'}
       
    }),
    then(response => {
    this.weather = response.data
    }).catch(error => {
    console.log(error)
    console.log(error.response.data)
    })
 }
},

created: function() {
this.getzillow(),
this.getweather()
},

})



