var app = angular.module("friendsApp", ["ngRoute"]);

app.config(function ($routeProvider) {
    $routeProvider
    .when("/new", {
        templateUrl: "/partials/new.html",
        controller: "newFriendController",
        // controller: "showFriendController" -- can't do this, need to add function below
    })
    .when("/edit/:id", {
        templateUrl: "/partials/edit.html",
        controller: "editFriendController"
    })
    .when("/show/:id", {
        templateUrl: "/partials/show.html",
        controller: "showFriendController"
    })
    .when("/", {
        templateUrl: "/partials/home.html",
        controller: "homeFriendController"
    })
    // .when("/delete/:id", {
    //     templateUrl: "/partials/home.html",
    //     controller: "deleteFriendController"
    // })
    .otherwise("/");
});

app.factory("friendFactory", function ($http) {
    var factory = {};
    var friends = [];

    factory.getFriend = function (friendId, receivedFriend) {
        $http.get("/api/friends/" + friendId).then(function (response) {
           receivedFriend(response.data.friend)

        })
    }

    factory.addFriend = function (friend, finishedAddingFriend) {
        $http.post("/api/friends", friend).then(function (response) {
            friends.push(response.data.friend);
            finishedAddingFriend();
        });
    }
    factory.allFriends = function (receivedFriends) {
        $http.get("/api/friends").then(function (response) {
            friends = response.data.friends;
            receivedFriends(friends);
            //console.log(friends)
        });
        //add function to add friends var from factory
        // receivedFriends(friends);
    }

    //testing this method for update, questionable
    factory.updateFriend = function (friend, receivedFriend) {

        $http.put('/api/friends/' + friend._id, {first_name: friend.first_name, last_name: friend.last_name, birthday: friend.birthday})
        .then(function(response) {
            console.log('hit response')
            friend=response.data;
            receivedFriend(friend)
        })
    }
    factory.deleteFriend = function(id, callback) {
        $http.delete('/api/friends/' + id);
        callback(friends)
        console.log('hit factory delete')
    }
    return factory;
})

app.controller("showFriendController", function ($scope, friendFactory, $routeParams) {
    friendFactory.getFriend($routeParams.id, function(friend) {
        $scope.friend=friend;
    })
});

app.controller("homeFriendController", function ($scope, friendFactory, $routeParams) {
    friendFactory.allFriends(function (friends) {
        $scope.friends = friends;
    });

    //add delete
    $scope.deleteFriend = function(id){
        friendFactory.deleteFriend($routeParams.id, function(friends) {
            $scope.friends=friends;
        })
    };
});

app.controller("newFriendController", function ($scope, friendFactory, $location) {
    friendFactory.allFriends(function (friends) {
        $scope.friends = friends;
    });

    $scope.addFriend = function () {
        friendFactory.addFriend($scope.friend, function () {
            $scope.friend = {};
            $location.url('/')
        });
    }
});

app.controller("editFriendController", function($scope, friendFactory, $routeParams, $location) {
    friendFactory.getFriend($routeParams.id, function(friend) {
        $scope.friend=friend;
    })
    $scope.updateFriend = function () {
        console.log("hitting .updateFriend")
        friendFactory.updateFriend($scope.friend, function() {
            $scope.updatedFriend = {};
        })
        $location.url("/")
    }

})



// app.controller("editFriendController", function ($scope, friendFactory) {
//     $scope.addFriend = function () {
//         friendFactory.addFriend($scope.friend, function () {
//             $scope.friend = {};
//         });
//     }
// });