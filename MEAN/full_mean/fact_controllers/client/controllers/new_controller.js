var app = angular.module('app');

app.controller('newController',
  [
    '$scope',
    'friendsFactory',
    function($scope, friendsFactory){

      //when your index.html page loads, you should see this line. Otherwise
      //make sure your controller syntax is correct
      //and that you have included the controller script file
      console.log('newController loaded');
      var self = this;

      // This line is optional, because angular will be smart enough
      // to know you have a NC.newFriend object from your ng-model.
      self.newFriend = {};
      // Using the ng-model on the view, angular will determine that
      // two properties will need to be added to this object: name and favoriteLanguage

      var index = function(){
        friendsFactory.index(function(returnedData){
          self.friends = returnedData;
        });
      };
      index();

      // Define a create function so that if someone clicks on
      // an element with ng-click="NC.create()"
      // it triggers the function and runs the code inside
      self.create = function(){
        console.log('Create Friend clicked!');
        //if the required fields are not submitted, then don't proceed
        if (!self.newFriend.name || !self.newFriend.favoriteLanguage) {
          console.log('required fields not present');
          return;
        }

        console.log("\n\nCREATE Step 1: The controller is calling the factory's create() function and passing a friend object and a callback:", self.newFriend);

        friendsFactory.create(self.newFriend, function(newFriendAfterServer){
          console.log("CREATE Step 5: The response data was sent back to the controller via a callback parameter:", newFriendAfterServer);
          self.createdFriend = newFriendAfterServer;
          console.log("CREATE Step 6: The data was then assigned to self/scope, so that the view will update with the new data.\n\n");
        });
      }
    } //close the function being passed into the controller
  ] // close array of injected services + controller function
); //end the controller function invocation: ()