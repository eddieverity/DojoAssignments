console.log('/server/controllers/products.js')

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

//create is messed up, need to fix
//#1 get single user by id
//#2 add product id to user.orders
//#3 grab single product by id
//#4 decrease quantity by order.quantity
//#5 create order in order model
module.exports.create=function(request,response){
  // find user by id, .push to array order id & quantity
  User.findOne({_id:request.params.userId}, function(err, user){
    if(err){
      console.log(err)
    } else {
      var asdf=user.name
      console.log(asdf)
      user.orders.push(request.params.productId)
      user.save(function(err,updatedUser){
        if(err){
          console.log(err)
        } else {
          Product.findOne({_id:request.params.productId}, function(err, product){
            if(err){
              console.log(err)
            } else {
              var qwer=product.name
              //resave product info pulled from findOne updating quantity
              product.quantity-=request.body.quantity;
              product.save(function(err,updatedProduct){
                if(err){
                  console.log(err)
                } else {      
                  var order= new Order({
                    quantity: request.body.quantity,
                    user: asdf,
                    product: qwer
                  })
                  //console.log(request.data.user)
                  order.save(function(err,newOrder){
                    if(err){
                      console.log(err)
                    } else {
                      response.json({message:"Created Order", order:newOrder, product:updatedProduct, user:updatedUser})
                    }
                  })
                }
              })
            }
          })
        }
      })
    }
  })
}