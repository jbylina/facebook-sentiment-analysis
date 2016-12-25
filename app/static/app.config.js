'use strict';

angular
  .module('sentimentApp')
  .config(['$routeProvider', '$locationProvider',
    function ($routeProvider, $locationProvider) {
      $locationProvider.html5Mode(true);
      $routeProvider
        .when('/', {
          template: '<page-input></page-input>'
        })
        .when('/chart', {
          template: '<page-input></page-input><chart></chart>'
        })
        .otherwise('/');
  }]);
