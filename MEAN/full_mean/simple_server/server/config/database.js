/*
    Database Config File
    also referred to as 'mongoose.js' in some assignments
*/
console.log("/server/config/database.js");
var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/friend", function (err) {
    if (err) {
        console.log(err);
    } else {
        console.log("Connected to Mongoose");
    }
});
require("../models/friend");  // Require Item DB Model