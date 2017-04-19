/*
    Route Request to Appropriate Contoller
*/
console.log("/server/config/routes.js");
var users = require("../controllers/schemas");  // Require Items Controller

module.exports = function (app)
{
    // app.get("/api/friends/:id", friends.show);
    // app.get("/api/friends", friends.home);
    // app.post("/api/friends", friends.create);
    // app.put("/api/friends/:id", friends.edit);
    // app.delete('/api/friends/:id', friends.delete);

    app.post("/api/users", users.register);
    app.post("/api/login", users.login);
    app.post("/api/posts", users.addpost);
    app.get("/api/posts", users.home);

    //added for comments
    app.post("/api/comments", users.addcomment);
    app.get("/api/comments", users.home);

    //^added for comments


}