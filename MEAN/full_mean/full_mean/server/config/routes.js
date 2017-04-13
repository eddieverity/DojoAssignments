/*
    Route Request to Appropriate Contoller
*/
console.log("/server/config/routes.js");
var items = require("../controllers/items");  // Require Items Controller

module.exports = function (app)
{
    app.get("/api/items", items.index);
    app.post("/api/items", items.create);
}