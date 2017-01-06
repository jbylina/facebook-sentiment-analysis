'use strict';

angular
    .module('sentimentAnalysisApp', [
        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngSanitize',
        'chart.js'
    ]).config(['$routeProvider', '$locationProvider',
    function ($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(true);
        $routeProvider
            .when('/', {
                templateUrl: 'new-analysis/new-analysis.tpl.html',
                controller: 'NewAnalysisCtrl'
            })
            .when('/chart/:pageUrl', {
                templateUrl: 'chart/chart.template.html',
                controller: 'ChartCtrl'
            })
            .otherwise('/');
    }]);
