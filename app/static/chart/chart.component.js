'use strict';

angular
  .module('chart')
  .component('chart', {
    templateUrl: 'chart/chart.template.html',
    controller: ['Analyze', '$routeParams', 
      function ChartController(Analyze, $routeParams) {
        var self = this;
        self.pageUrl =  $routeParams.pageUrl;
        // send page request
        var response = Analyze.query({pageUrl:self.pageUrl});
        response.$promise.then(function (data) {
          var items = response.results;
          self.results = [items.positive, items.neutral, items.negative];
        });
      }
    ]
  });
