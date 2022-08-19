var searchQuotesApp = new Vue({
  el: '#searchQuotesApp',
  data: {
      searchText: '',
      searchType: 'keyword',
      quotes: [],
      shouldPaginate: false,
      page: { pageNumber: 0,
              isLastPage: true}
  },
  methods: {
      search: function(pageNumber = 0) {
          let urlParameters = {   filter: this.searchText,
                                  type: this.searchType };
          if (pageNumber > 0) {
              urlParameters.page = pageNumber;
          }

          axios({
              method: 'get',
              url: 'https://favqs.com/api/quotes',
              params: urlParameters,
              headers: {
                  "Authorization": `Token token="8f11f41caeb544443c9e3062693e97b1"`
              }
          }).then((response) => {
              this.quotes.length = 0;
              let resultsLength = response.data.quotes.length;

              for (let i = 0; i < resultsLength; i++) {
                  this.quotes.push(response.data.quotes[i]);
              }

              this.page = {   pageNumber: response.data.page,
                              isLastPage: response.data.last_page };

              if (this.page.pageNumber <= 1 && (this.page.isLastPage == true || this.quotes[0].body === "No quotes found")) {
                  this.shouldPaginate = false;
                  this.page.pageNumber = 0;
              }
              else {
                  this.shouldPaginate = true;
              }
          });
      },
      loadRandomQuotes: function() {
          for (var i = 0; i < 5; i++)
          {
              this.getRandomQuote();
          }
      },
      getRandomQuote: function() {
          axios({
              method: 'get',
              url: 'https://favqs.com/api/qotd',
          }).then((response) => {
              this.quotes.push(response.data.quote);
          }).catch(error => {
              // TODO: handle error
              console.log(error);
          });
      }
  },
  created: function() {
      this.loadRandomQuotes();
  }
});


Vue.component('pagination', {
  props: ['page'],
  methods: {
      pageRange: function(pageNumber) {
          var list = [];
          end = pageNumber - 1;
          start = (end < 4) ? 1 : end - 3;
          for (let i = start; i <= end; i++) {
              list.push(i);
          }
          return list;
      }
  },
  template: `
  <p class="pagination center-align">
      <span :class="[(page.pageNumber <= 1) && 'disabled']"><a href="#!" v-on:click="$emit(\'search\', (page.pageNumber - 1))"><i class="material-icons">chevron_left</i></a></span>
      <span v-for="pageNum in pageRange(page.pageNumber)" class="waves-effect"><a href="#!" v-on:click="$emit(\'search\', pageNum)">{{pageNum}}</a></span>
      <span class="active"><a href="#!">{{page.pageNumber}}</a></span>
      <span :class="[page.isLastPage && 'disabled']"><a href="#!" v-on:click="$emit(\'search\', (page.pageNumber + 1))"><i class="material-icons">chevron_right</i></a></span>
  </p>
  `
});
