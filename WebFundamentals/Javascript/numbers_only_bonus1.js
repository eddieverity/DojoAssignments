// write a second function that removes them from the current array

function onlyNums(arr) {
  for (var i=0;i<arr.length;i++) {
    if (typeof arr[i] !== "number") {
      arr.splice(i,1);
    }
  }
  return(arr);
}
onlyNums(["Frank",42,0,"23",-1000,10000,11,"asdf",12]);