var mongoose=require('mongoose');


var orderSchema=mongoose.Schema({
  quantity:Number,
  user: String,
  product: String,

}, {timestamps:true})

mongoose.model("Order", orderSchema);