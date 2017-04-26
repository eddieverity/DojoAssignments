var app=angular.module('storeApp', ['ngRoute']);
app.config(function($routeProvider){
  $routeProvider
  .when('/', {
    templateUrl: '/partials/home.html',
    controller: 'homeCtrl'
  })
  .when('/orders', {
    templateUrl: '/partials/orders.html',
    controller: 'ordersCtrl'
  })
  .when('/products', {
    templateUrl: '/partials/products.html',
    controller: 'productsCtrl'
  })
  .when('/customers', {
    templateUrl: '/partials/customers.html',
    controller: 'usersCtrl'
  })
  .otherwise('/')
})


////////////////////    FACTORIES   //////////////////////
app.factory('userFactory', function($http){
  var factory={};

  factory.getAllUsers=function(foundUsers){
    $http.get('/api/users').then(function(response){
      foundUsers(response.data.users)
    })
  }

  factory.createUser=function(user, createdUser){
    $http.post('/api/users', user).then(function(response){
      createdUser(true)
    }).catch(function(error){
      createdUser(false);
    })
  }

  factory.deleteUser=function(id,callback){
    $http.delete('/api/users/'+id).then(function(response){
      callback(response.data.message)
    })
  }

  factory.createOrder=function(userId,productId,order,callback){
    $http.post('api/orders/'+userId+'/'+productId, order).then(function(response){
      callback(response.data.message)
    })
  }



  return factory;
})

app.factory('productFactory', function($http){
  var factory={};
  factory.getAllProducts=function(foundProducts){
    $http.get('/api/products').then(function(response){
      foundProducts(response.data.products)
    })
  }
  factory.createProduct=function(product,createdProduct){
    $http.post('/api/products', product).then(function(response){
      createdProduct(true)
    }).catch(function(error){
      createdProduct(false);
    })
  }
  return factory;
})

app.factory('orderFactory', function($http){
  var factory={};
  factory.getAllOrders=function(foundOrders){
    $http.get('/api/orders').then(function(response){
      foundOrders(response.data.orders)
    })
  }
  return factory;
})


///////       CONTROLLERS  /////////////////
app.controller('ordersCtrl', function($scope,productFactory,userFactory,orderFactory,$routeParams){
  productFactory.getAllProducts(function(products){
    $scope.products=products
    userFactory.getAllUsers(function(users){
      $scope.users=users;
      orderFactory.getAllOrders(function(orders){
        $scope.orders=orders;
      })
    })
  })

  $scope.addOrder=function(){
    userId=$scope.order.userId._id
    productId=$scope.order.productId._id
    console.log(userId)
    userFactory.createOrder(userId,productId,$scope.order, function(success){
      if(success){
        console.log('success')
        productFactory.getAllProducts(function(products){
          $scope.products=products
          userFactory.getAllUsers(function(users){
            $scope.users=users;
            orderFactory.getAllOrders(function(orders){
              $scope.orders=orders;
            })
          })
        })
      } else {
        console.log('error creating order in ordersCtrl.addOrder')
      }
    })
  }
})

app.controller('productsCtrl', function($scope,productFactory,$location){
  productFactory.getAllProducts(function(products){
    $scope.products=products
  })
  $scope.createProduct=function(){
    productFactory.createProduct($scope.product, function(success){
      if(success){
        console.log('success')
      } else {
        console.log('error creating product')
      }
    })
    productFactory.getAllProducts(function(products){
      $scope.products=products
    })
  }
})

app.controller('homeCtrl', function($scope,userFactory,productFactory,orderFactory){
  productFactory.getAllProducts(function(products){
    $scope.products=products
    userFactory.getAllUsers(function(users){
      $scope.users=users;
      orderFactory.getAllOrders(function(orders){
        $scope.orders=orders;
      })
    })
  })
})

app.controller('usersCtrl', function($scope,userFactory,$location){
  userFactory.getAllUsers(function(users){
    $scope.users=users;
  })
  $scope.createUser=function(){
    userFactory.createUser($scope.user, function(success){
      if(success){
        console.log('success')
      } else {
        console.log('error creating user')
      }
    })
    userFactory.getAllUsers(function(users){
      $scope.users=users;
    })

  }
  $scope.deleteUser=function(id){
    userFactory.deleteUser(id, function(message){

      userFactory.getAllUsers(function(users){
        $scope.users=users;
      })

    })
  }
})



