'use strict';

angular
    .module('sentimentAnalysisApp')
    .controller('ChartCtrl', ['$scope', 'Analyze', '$routeParams', function ($scope, Analyze, $routeParams) {
        var self = this;
        $scope.pageUrl = $routeParams.pageUrl;
        // send page request
        Analyze.query({pageUrl: $routeParams.pageUrl}, function (data) {
            var items = data.results;
            $scope.results = [items.positive, items.neutral, items.negative];
            $scope.labels = [items.positive.text, items.neutral.text, items.negative.text];
            $scope.data = [items.positive.count, items.neutral.count, items.negative.count];
        });
    }]);
