var hello = "interesting";
function example() {
  var hello = "hi!";
  console.log(hello);
}
example();
console.log(hello);

//declarations get hoisted
var hello;                 
function example() {       
  var hello;               
  hello = "hi";            
  console.log(hello);       
}
//assignments and invocation maintain order
hello = "interesting";     
example();                        
console.log(hello);