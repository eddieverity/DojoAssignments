var my_module = require('./mathlib')();     //notice the extra invocation parentheses!
// console.log(mathlib);

my_module.add(5,8);
my_module.multiply(5,8);
my_module.square(5);
my_module.random(5,20)
