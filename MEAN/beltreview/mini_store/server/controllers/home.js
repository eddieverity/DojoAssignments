console.log('/server/controllers/home.js')

var mongoose=require('mongoose');
var Product=mongoose.model('Product');
var User=mongoose.model('User');
var Order=mongoose.model('Order')

module.exports.index=function(request,response){
  Product.find({}, function(err,products){
    if(err){
      console.log(err)
    } else {
      User.find({}, function(err,users){
        if(err){
        console.log(err)
        } else {
          Order.find({}, function(err,orders){
            if(err){
            console.log(err)
            } else {
              response.json({message:'Orders Index', orders:orders, users:users, products:products})
            }
          })
        }
      })
    }
  })
}
