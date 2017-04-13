/*
    Item DB Model
*/
console.log("/server/models/item.js");

var mongoose = require("mongoose");
var itemSchema = mongoose.Schema({
    title: String,
    dueDate: Date
}, { timestamps: true });
mongoose.model("Item", itemSchema);