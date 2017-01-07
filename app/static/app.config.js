'use strict';

angular
    .module('sentimentAnalysisApp', [
        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngSanitize',
        'chart.js',
        'btford.socket-io'
    ]).config(['$routeProvider', '$locationProvider',
    function ($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(true);
        $routeProvider
            .when('/', {
                templateUrl: 'home/home.tpl.html',
                controller: 'HomeCtrl'
            })
            .when('/newAnalysis/:pageUrl', {
                templateUrl: 'new-analysis/new-analysis.template.html',
                controller: 'NewAnalysisCtrl'
            })
            .otherwise('/');
    }]);
