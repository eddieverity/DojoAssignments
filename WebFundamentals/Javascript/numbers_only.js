function onlyNums(arr) {
  var newArray = [];
  for (var i=0;i<arr.length;i++) {
    if (typeof arr[i] === "number") {
      newArray.push(arr[i]);
    }
  }
  return(newArray);
}
onlyNums(["Frank",42,0,"42",-1000,10000,true,"blue"]);