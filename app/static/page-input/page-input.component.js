'use strict';

angular
  .module('pageInput')
  .component('pageInput', {
    templateUrl: 'page-input/page-input.template.html',
    controller: ['$location', '$routeParams',
      function PageInputController($location, $routeParams) {
        var self = this;
        self.targetUrl = $routeParams.pageUrl;
        self.analyzePage = function analyzePage(pageUrl) {
          console.log($location.absUrl()); //TODO check&rmv
          $location.path('/chart').search({pageUrl: pageUrl});
          console.log($location.absUrl()); //TODO check&rmv
        };
      }
    ]
  });
