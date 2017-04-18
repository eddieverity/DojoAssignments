/*
    Route Request to Appropriate Contoller
*/
console.log("/server/config/routes.js");
var friends = require("../controllers/friends");  // Require Items Controller

module.exports = function (app)
{
    app.get("/api/friends/:id", friends.show);
    app.get("/api/friends", friends.home);
    app.post("/api/friends", friends.create);
    app.put("/api/friends/:id", friends.edit);
    app.delete('/api/friends/:id', friends.delete);

}