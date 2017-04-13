var app = angular.module("itemsApp", ["ngRoute"]);

app.config(function ($routeProvider) {
    $routeProvider
    .when("/new", {
        templateUrl: "/partials/new-item.html",
        controller: "newItemController"
    })
    .when("/index", {
        templateUrl: "/partials/items-index.html",
        controller: "itemsIndexController"
    })
    .otherwise("/index");
});
app.factory("itemFactory", function ($http) {
    var factory = {};
    var items = [
        { title: "Do Stuff", dueDate: new Date() },
        { title: "Do More Stuff", dueDate: new Date() },
        { title: "Do Even More Stuff", dueDate: new Date() },
    ];

    factory.addItem = function (item, finishedAddingItem) {
        $http.post("/api/items", item).then(function (response) {
            items.push(response.data.item);
            finishedAddingItem();
        });
    }
    factory.allItems = function (receivedItems) {
        $http.get("/api/items").then(function (response) {
            items = response.data.items;
            receivedItems(items);
        });
    }

    return factory;
})
app.controller("itemsIndexController", function ($scope, itemFactory) {
    itemFactory.allItems(function (items) {
        $scope.items = items;
    });
});
app.controller("newItemController", function ($scope, itemFactory) {
    $scope.addItem = function () {
        console.log("NEW ITEM:", $scope.item);
        itemFactory.addItem($scope.item, function () {
            $scope.item = {};
        });
    }
});