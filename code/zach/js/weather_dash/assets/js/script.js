const API_KEY = '66fcfa1d817633c15bf549048210a95c';
const defCity = 'new york'


const app1 = new Vue({
  el: '#app-1',
  data: {
    message: 'Hello Vue!',
    cWeather: {},
    fWeather: {},
    topCities: ['Charleston', 'New York', 'London', 'Hong Kong'],
    cityInput: '',
  },
  methods: {
    getWeatherData: function (cityName, API_KEY) {
      let url = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${API_KEY}&units=imperial`;
      axios
        .get(url)
        .then((response) => {
          this.cWeather = response.data;
          console.log(this.cWeather);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getForecastData: function (cityName, API_KEY) {
      let url = `https://api.openweathermap.org/data/2.5/forecast?q=${cityName}&appid=${API_KEY}&units=imperial`;
      axios
        .get(url)
        .then((response) => {
          this.fWeather = response.data;
          console.log(this.fWeather);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    onClick() {
      console.log(this.cityInput)
      let citySearch = this.cityInput
      this.getWeatherData(citySearch, API_KEY)
      this.getForecastData(citySearch, API_KEY)
    },
  },
   created: function () {
    this.getForecastData(defCity, API_KEY);
    this.getWeatherData(defCity, API_KEY);
  },
});


