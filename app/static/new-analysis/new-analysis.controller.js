'use strict';

angular
    .module('sentimentAnalysisApp')
    .controller('NewAnalysisCtrl', ['$scope', 'Analyze', 'RealtimeAnalyze', '$routeParams',
        function ($scope, Analyze, RealtimeAnalyze, $routeParams) {

            $scope.processLogs = [];
            
            Analyze.processPage({"pageUrl": $routeParams.pageUrl}, function (data) {
                $scope.pageUrl = data.pageUrl + ' ' + data.taskId;

                RealtimeAnalyze.on(data.pageUrl, function (data) {
                    $scope.processLogs.unshift({
                        date: new Date(),
                        message: JSON.stringify(data)
                    })
                });

                var items = data.results;
                $scope.results = [items.positive, items.neutral, items.negative];
                $scope.labels = [items.positive.text, items.neutral.text, items.negative.text];
                $scope.data = [items.positive.count, items.neutral.count, items.negative.count];
            });
        }]);
