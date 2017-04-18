/*
    Database Config File
    also referred to as 'mongoose.js' in some assignments
*/
console.log("/server/config/mongoose.js");
var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/walldb", function (err) {
    if (err) {
        console.log(err);
    } else {
        console.log("Connected to Mongoose");
    }
});
require("../models/schema");  // Require Item DB Model