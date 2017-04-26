console.log('/server/controllers/users.js')

var mongoose=require('mongoose');
var User=mongoose.model('User');
var Order=mongoose.model('Order')

module.exports.index=function(request,response){
  User.find({}, function(err,users){
    if(err){
      console.log(err)
    } else {
      response.json({message:'Users Index', users:users})
    }
  })
}

module.exports.create=function(request,response){
  var user=new User({
    name:request.body.name,
  })
  user.save(function(err){
    if(err){
      console.log(err)
    } else {
      response.json({
        message:'Successfully added User',
        user:user
      })
    }
  })
}

module.exports.delete=function(request,response){
  User.remove({_id:request.params.id},function(err){
    if(err){
      console.log(err)
    } else {
      response.json({message:'Deleted User'});
    }
  })
}