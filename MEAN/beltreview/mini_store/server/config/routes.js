
console.log("/server/config/routes.js");

var users=require("../controllers/users");
var products=require("../controllers/products");
var orders=require("../controllers/orders");
var home=require("../controllers/home")


module.exports=function(app)
{
  app.get("api/home", home.index)

  app.get("/api/users", users.index)
  app.post("/api/users", users.create)
  app.delete("/api/users/:id", users.delete)

  app.get("/api/products", products.index)
  app.post("/api/products", products.create)

  app.get("/api/orders", orders.index)
  app.post("/api/orders/:userId/:productId", orders.create)
}