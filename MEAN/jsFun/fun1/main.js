function iterator(arr) {
  for (var i = 0;i<arr.length; i++) {
    console.log(arr[i]);
  }
}

var x = [3,5,"Dojo", "rocks", "Mike", "Sensei"];
iterator(x);
x.push(100);
x.push(["hello", "world", "JavaScript is Fun"]);
console.log(x);

var total=0;
for (var i = 0;i<501;i++) {
  total+=i;
}
console.log(total);

var arrcheck=[1,5,90,25,-3,0]
var min=0;
var avgtotal=0;
for (var i =0;i<arrcheck.length;i++) {
  if (arrcheck[i]<min) {
    min = arrcheck[i];
  }
}
console.log(min);

for (var i=0;i<arrcheck.length;i++) {
  avgtotal+=arrcheck[i];
}
var avg=avgtotal/arrcheck.length;
console.log(avg);

var newNinja = {
  name: 'Jessica',
  profession: 'coder',
  favorite_language: 'JavaScript', //like that's even a question!
  dojo: 'Dallas'
}

for (idx in newNinja) {
  console.log(idx);
  console.log(newNinja[idx]);
}

