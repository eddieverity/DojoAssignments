/*
    Handle Incoming Requests for Items
*/
console.log("/server/controllers/friends.js");

var mongoose = require("mongoose");
var User = mongoose.model("User");
var Post = mongoose.model("Post");
var Comment = mongoose.model("Comment")


module.exports.home = function (request, response) {
    //console.log(request.data)

    Post.find({}).populate("_author").then(function (posts) {
      Comment.find({}).populate("_author _post").then(function (comments) {
          response.json({ posts: posts, comments: comments });
      }).catch(function (err) {
        console.log(err)
      })
    }).catch(function (err) {
      console.log(err)
    })

}


//cmd+shft+p for sublime stuffs // install

module.exports.login = function(request, response) {
    User.findOne({email: request.body.email}, function(err, user){ 

      if(err){
        console.log(err)
        response.json({errors:err});
      } 
      else if(user&&user.validPassword(request.body.password)) {
        response.json({
          id:user._id,
          username:user.username
        });
      }
      else if(user&& !user.validPassword(request.body.password)) {
        response.json({
          errors: {
            login: {
              message: "Password isn't correct"
            }
          },

        })
      }
      else {
        response.json({
          errors: {
            login: {
              message:"Email not found, try to register"
            }
          }
        })
      }
    })
}

module.exports.register = function (request, response) {
    var user = new User(request.body);
    user.save(function (err) {
        if (err) {
            response.json({errors: err})
            // console.log(err);
        } else {
            response.json({ message: "Successfully Created User!", user: user });
        }
    });
}

module.exports.addpost = function (request, response) {
    var post = new Post(request.body);
    post.save(function(err, newpost) {
      if (err) {
        console.log(err);
      } else {
        response.json({posttext:newpost.posttext, author:newpost.author})
      }
    })
}

module.exports.addcomment = function (request, response) {
    var comment = new Comment(request.body);
    comment.save(function(err, newcomment) {
      if (err) {
        console.log(err);
      } else {
        response.json({commenttext:newcomment.commenttext, author:newcomment.author})
      }
    })
}

