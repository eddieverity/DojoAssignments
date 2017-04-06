function myDoubleConsoleLog(arg1, arg2) {
  if (typeof arg1==='function'){
    console.log(arg1());
  }
  if (typeof arg2==='function'){
    console.log(arg2());
  }
}