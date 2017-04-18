var app = angular.module("app", ["ngRoute", "ngMessages", "ngCookies"]);

app.config(function ($routeProvider) {
  $routeProvider
  .when("/login", {
    templateUrl: "/partials/login.html",
    controller: "loginController",
  })
  .when("/", {

    templateUrl: "/partials/home.html",
    controller: "homeController",

    resolve: {

      getComments: function(commentFactory){
        return commentFactory.getComments(function(comments){
          
          
        });
        var allcomments=comments
        console.log(comments)
      },
      getPosts: function(postFactory){
        return postFactory.getPosts(function(posts){
          var allPosts=posts
          console.log(posts)
        });
      
      }

    }
  })
  .otherwise("/");
})

app.factory("userFactory", function($http) {
  var factory={};
  factory.user=null;

  factory.register = function(user, finishedAddingUser){
    $http.post('/api/users', user).then(function(response) {
      factory.user= { id: response.data.user._id,
        username: response.data.user.username
      }
    finishedAddingUser();
    })
  }

  return factory;
})

app.factory("postFactory", function($http){
  var factory={};
  var posts =[];

  factory.getPosts = function(receivedPosts) {
    $http.get("/api/posts").then(function(response){
      posts=response.data.posts;
      receivedPosts(posts)
    })
  }
  factory.addNewPost = function(postdata, finishedAddingPost){
    $http.post('/api/posts', postdata).then(function(response) {
        finishedAddingPost();
      }
    )
  }

  return factory;
})

app.factory("commentFactory", function($http){
  var factory={};
  var comments =[];

  factory.getComments = function(receivedComments) {
    $http.get("/api/comments").then(function(response){
      comments=response.data.comments;
      receivedComments(comments)
    })
  }
  factory.addNewComment = function(postdata, finishedAddingComment){
    $http.post('/api/comments', postdata).then(function(response) {
        finishedAddingComment();
      }
    )
  }

  return factory;
})

app.controller("loginController", function($scope, $location, userFactory, $cookies){
  $scope.register=function() {
    if ($scope.registerUser.password==$scope.registerUser.confirm){  
      userFactory.register($scope.registerUser, function(){
        $cookies.put('loggeduserid', userFactory.user.id);
        $cookies.put('loggedusername', userFactory.user.username);
        var favcookie = $cookies.get('loggedusername')
        $location.url('/')
      })
    }
  }
  //add login function
})

app.controller("homeController", function($scope, $location, userFactory, postFactory, commentFactory, $cookies, $route, getComments, getPosts){
  var id = $cookies.get("loggeduserid")
  var name = $cookies.get("loggedusername")
  $scope.user={id:id, username:name}
  $scope.posts=getPosts
  $scope.comments=getComments
  //new test comments
  // postFactory.getPosts(function(posts){
  //   $scope.posts=posts
  // })

  // commentFactory.getComments(function(comments){
  //   $scope.comments=comments
  // })
  //new test comments

  // $scope.newcomment = {};

  // commentFactory.getComments(function(comments){

  //   $scope.comments=comments
  //   console.log(comments)
  // })
  
  $scope.addPost=function(){
    var newpostdata = { postText: $scope.newpost.posttext, _author: $scope.user.id}
    postFactory.addNewPost(newpostdata, function(){
      $scope.newpost={};
    })
    $route.reload();
  }

  $scope.addComment=function(postidfrompage, newcomment){

    var newcommentdata = { 
      commentText: newcomment.commenttext,
      _author: $scope.user.id,
      _post:postidfrompage
    }

    commentFactory.addNewComment(newcommentdata, function(){
      $scope.newcomment={};
    })
    $route.reload();
  }

})