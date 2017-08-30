var main_app = angular.module("main_app", []);

main_app.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

main_app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{&');
  $interpolateProvider.endSymbol('&}');
});

main_app.controller("main_app_controller", function ($scope, $http) {
   $scope.formmodule=new FormData();
   var file={};
   $scope.upload = function(forminput) {
    file = forminput.files[0];
    };

   $scope.str= "";
   $scope.str1=[];
   $scope.arr=[];

   $scope.OnSubmit=function () {
       $scope.formmodule.append("name",$scope.name)
       $scope.formmodule.append("file", file)
       $http({
           method:'POST', data:$scope.formmodule, url:"", transformRequest:angular.identity, headers:{ 'Content-Type':undefined}
       }).then(function (response) {
         $scope.str=response.data.toString();
         $scope.str1=response.data.split(',');
         console.log(response.data.toString());
         for(var i=0; i<$scope.str1.length; i++){
            $scope.arr[i]=[i, parseFloat($scope.str1[i])];
          }
         console.log($scope.arr.length);
       })


       google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('number', 'X');
        data.addColumn('number', 'Данные');


        data.addRows($scope.arr);

        var options = {
          title: 'График',
          //curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }

   }
});