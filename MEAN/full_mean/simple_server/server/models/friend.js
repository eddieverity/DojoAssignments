/*
    Item DB Model
*/
console.log("/server/models/friend.js");

var mongoose = require("mongoose");
var friendSchema = mongoose.Schema({
    first_name: String,
    last_name: String,
    birthday: Date
}, { timestamps: true });
mongoose.model("Friend", friendSchema);