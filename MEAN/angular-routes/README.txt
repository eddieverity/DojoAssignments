-- bower init
    hit enter a bunch of times

-- bower install angular --save
-- bower install angular-route --save

-- npm init -y
-- npm install express --save

open in sublime

-- in main directory mkdir client
-- in client, make index.html (express will auto-load index.html page)
-- in client, make partials sub-folder
-- inside partials folder, make partial .html files

-- make server.js file in main directory

server.js--

var express=require('express'),
app = express(),
path = require('path');

app.use(express.static(path.join(__dirname, './client')));
app.use(express.static(path.join(__dirname, './bower_components')));

app.listen(8000, function() {
  console.log( `server running on port ${ port }` );
});

--server.js

--nodemon server.js (will autoload index.html file)

index.html--

boilerplate html
add--
<html lang-"en" ng-app ='app'>

<script src="/angular/angular.js" charset="utf-8"></script>
<script src="/angular-route/angular-route.js" charset="utf-8"></script>
<script> // goods go here
  var app=angular.module('app', ['ngRoute']);
  app.config(function($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'partials/partial1.html'
    })
    .when('/partial2', {
      templateUrl: 'partials/partial2.html'
    })
    .otherwise({
      redirectTo: '/'
    })
  })

</script>

<body>
<div ng-view>
  //partials will load in here//
</div>
<a href='#'>Partial1</a>
<a href="#/partial2">Partial2</a>

---end index.html





