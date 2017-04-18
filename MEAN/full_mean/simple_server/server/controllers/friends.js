/*
    Handle Incoming Requests for Items
*/
console.log("/server/controllers/friends.js");

var mongoose = require("mongoose");
var Friend = mongoose.model("Friend");


module.exports.home = function (request, response) {
    Friend.find({}, function (err, friends) {
        if (err) {
            console.log(err);
        } else {
            response.json({ message: "Friends Index", friends: friends });
        }
    });
}

module.exports.show = function (request, response) {
    console.log("hit module.exports.show function")
    Friend.findOne({_id: request.params.id}, function(err, friend){
        
        response.json({friend:friend});
    })
}

module.exports.create = function (request, response) {
    console.log("hit create function in friends.js")
    var friend = new Friend({
        first_name: request.body.first_name,
        last_name: request.body.last_name,
        birthday: request.body.birthday
    });
    console.log("friend = " + friend);
    friend.save(function (err) {
        if (err) {
            console.log(err);
        } else {
            response.json({ message: "Successfully Created Friend!", friend: friend });
        }
    });
}

module.exports.edit = function (request, response) {
    //this is jacked up, fix to an edit
    Friend.findOne({ _id: request.params.id }, function(err, friend) {
        if (err){
            console.log(err);
        }
        else {
            friend.first_name = request.body.first_name;
            friend.last_name = request.body.last_name;
            friend.birthday = request.body.birthday;
            friend.save(function(err, updatedFriend) {
                if (err){
                    console.log(err)
                }
                else {
                    resonse.json(updatedFriend)
                }
            })
        }
    })
}

module.exports.delete = function (request, response) {
    Friend.remove({ _id: request.params.id}, function(err) {
        if(err){
            console.log(err)
        } else {
            resonse.json({message:"Friend Deleted"})
        }
    })
}
