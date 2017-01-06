'use strict';

angular
    .module('sentimentAnalysisApp')
    .controller('NewAnalysisCtrl', ['$scope', '$location', '$routeParams', function ($scope, $location) {
        $scope.analyzePage = function analyzePage(pageUrl) {
            $location.path('/chart/' + encodeURIComponent(pageUrl));
        };
    }]);
