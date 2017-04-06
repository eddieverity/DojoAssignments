function myDoubleConsoleLog(arg1, arg2) {
  if (typeof arg1=='function'){
    console.log(arg1());
  }
  if (typeof arg2=='function'){
    console.log(arg2());
  }
}


function caller2(param){
  console.log('starting');
  // setTimeout(2000);
  // if (typeof(param)=='function'){
  //   setTimeout(param(),2000);
  // }

  setTimeout(function(){
    if (typeof param==="function"){
      param();
    }
  },2000);

  console.log('ending?');
  return 'interesting';
}
caller2(myDoubleConsoleLog('one','two'));

