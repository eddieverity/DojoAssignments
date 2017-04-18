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
        response.json({ posts: posts });
    }).catch(function (err) {
      console.log(err)
    })

    Comment.find({}).populate("_author _post").then(function (comments) {
        response.json({ comments: comments });
    }).catch(function (err) {
      console.log(err)
    })

}


//cmd+shft+p for sublime stuffs // install

module.exports.login = function (request, response) {
    User.findOne({_id: request.params.id}, function(err, user){  
        response.json({user:user});
    })
}

module.exports.register = function (request, response) {

    var user = new User(request.body);
    user.save(function (err) {
        if (err) {
            console.log(err);
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


// module.exports.delete = function (request, response) {
//     Friend.remove({ _id: request.params.id}, function(err) {
//         if(err){
//             console.log(err)
//         } else {
//             resonse.json({message:"Friend Deleted"})
//         }
//     })
// }