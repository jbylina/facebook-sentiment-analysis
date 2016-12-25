'use strict';

angular.
  module('core.analyze').
  factory('Analyze', ['$resource',
    function($resource) {
      return $resource('/api/analyze/', {}, {
        query: {
          method: 'GET',
          params: {pageUrl: ""}
        }
      });
    }
  ]);