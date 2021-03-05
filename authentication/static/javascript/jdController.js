'use strict';



app.controller('jdController', function($scope) {

    $scope.user = {
        password: "",
        confirmPassword: ""
    };


});

app.config(function($locationProvider,$interpolateProvider){
    $locationProvider.html5Mode({
              enabled:true
    });
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
 });






app.directive("compareTo", function ()
{

    return {
        require: "ngModel",
        scope:
        {
            confirmPassword: "=compareTo"
        },
        link: function (scope, element, attributes, modelVal)
        {
            modelVal.$validators.compareTo = function (val)
            {
                return val == scope.confirmPassword;
            };
            scope.$watch("confirmPassword", function ()
            {
                modelVal.$validate();
            });
        }
    };

});
