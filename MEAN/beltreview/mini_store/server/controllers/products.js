console.log('/server/controllers/products.js')

var mongoose=require('mongoose');
var Product=mongoose.model('Product');
var Order=mongoose.model('Order')

module.exports.index=function(request,response){
  Product.find({}, function(err,products){
    if(err){
      console.log(err)
    } else {
      response.json({message:'Products Index', products:products})
    }
  })
}

module.exports.create=function(request,response){
  var product=new Product({
    name:request.body.name,
    img:request.body.img,
    description:request.body.description,
    quantity:request.body.quantity
  })
  product.save(function(err){
    if(err){
      console.log(err)
    } else {
      response.json({
        message:'Successfully added Product',
        product:product
      })
    }
  })
}

