var mongoose=require('mongoose');


var productSchema=mongoose.Schema({
  name:String,
  img:String,
  description:String,
  quantity:Number,
}, {timestamps:true})

mongoose.model("Product", productSchema);