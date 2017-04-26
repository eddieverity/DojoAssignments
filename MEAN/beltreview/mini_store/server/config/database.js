console.log("/server/config/database.js");
var mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/mini_store", function (err) {
    if (err) {
        console.log(err);
    } else {
        console.log("Connected to Mongoose");
    }
});
require("../models/user");
require("../models/product");
require("../models/order")