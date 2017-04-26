var mongoose=require('mongoose');

var userSchema=mongoose.Schema({
  name:String,
  orders: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: "Product"
  }]
}, {timestamps:true})

mongoose.model("User", userSchema);