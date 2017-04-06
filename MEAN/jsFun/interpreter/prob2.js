var food = "Chicken";
function eat() {
  food = "half-chicken";
  console.log(food);
  var food = "gone";       // CAREFUL!
  console.log(food);
}
eat();
console.log(food);

//rearrangement

var food;
function eat() {
  var food;
  food = "half-chicken";
  console.log(food);

  food = "gone";       // CAREFUL!
  console.log(food);
}
food="chicken";
eat();
console.log(food);