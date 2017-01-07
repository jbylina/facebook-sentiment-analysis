'use strict';

angular
    .module('sentimentAnalysisApp')
    .controller('HomeCtrl', ['$scope', '$location', '$routeParams', function ($scope, $location) {
        $scope.analyzePage = function analyzePage(pageUrl) {
            $location.path('/newAnalysis/' + encodeURIComponent(pageUrl));
        };
    }]);
